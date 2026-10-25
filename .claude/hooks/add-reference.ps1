Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Write-HookContext {
    param([string]$Message)

    @{
        hookSpecificOutput = @{
            hookEventName    = 'UserPromptSubmit'
            additionalContext = $Message
        }
    } | ConvertTo-Json -Depth 5 -Compress
}

function Get-TitleKey {
    param([string]$Title)

    $name = [System.IO.Path]::GetFileNameWithoutExtension($Title)
    $name = $name -replace '(_논문_번역|논문_번역|_translation|_translated|번역본)$', ''
    $name = $name -replace '[_-]+', ' '
    $name = $name.ToLowerInvariant() -replace '[^\p{L}\p{Nd}]+', ' '
    return ($name -replace '\s+', ' ').Trim()
}

function Get-TokenSimilarity {
    param(
        [string]$Left,
        [string]$Right
    )

    if ($Left -eq $Right) {
        return 1.0
    }

    if ($Left.Length -ge 12 -and ($Left.Contains($Right) -or $Right.Contains($Left))) {
        return 0.95
    }

    $leftTokens = @($Left -split ' ' | Where-Object { $_.Length -gt 1 } | Select-Object -Unique)
    $rightTokens = @($Right -split ' ' | Where-Object { $_.Length -gt 1 } | Select-Object -Unique)
    if ($leftTokens.Count -eq 0 -or $rightTokens.Count -eq 0) {
        return 0.0
    }

    $rightSet = @{}
    foreach ($token in $rightTokens) {
        $rightSet[$token] = $true
    }

    $shared = 0
    foreach ($token in $leftTokens) {
        if ($rightSet.ContainsKey($token)) {
            $shared++
        }
    }

    return [double]$shared / ($leftTokens.Count + $rightTokens.Count - $shared)
}

function Get-RelativePath {
    param(
        [string]$Path,
        [string]$ProjectRoot
    )

    return $Path.Substring($ProjectRoot.Length).TrimStart('\', '/') -replace '\\', '/'
}

function Test-NonEmptyText {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        return $false
    }

    try {
        $text = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
        return -not [string]::IsNullOrWhiteSpace($text)
    } catch {
        return $false
    }
}

try {
    $hookInput = [Console]::In.ReadToEnd() | ConvertFrom-Json
    $prompt = [string]$hookInput.prompt
    $commandMatch = [regex]::Match($prompt, '(?s)^\s*/add\s+(?<title>.+?)\s*$')
    if (-not $commandMatch.Success) {
        exit 0
    }

    $requestedTitle = $commandMatch.Groups['title'].Value.Trim()
    if ($requestedTitle.Length -ge 2 -and (
        (($requestedTitle[0] -eq [char]34) -and ($requestedTitle[$requestedTitle.Length - 1] -eq [char]34)) -or
        (($requestedTitle[0] -eq [char]39) -and ($requestedTitle[$requestedTitle.Length - 1] -eq [char]39))
    )) {
        $requestedTitle = $requestedTitle.Substring(1, $requestedTitle.Length - 2).Trim()
    }

    if ([string]::IsNullOrWhiteSpace($requestedTitle)) {
        Write-HookContext 'Reference-add request: no paper title was supplied after /add. Ask for the exact title and do not change files.'
        exit 0
    }

    $requestedTitle = $requestedTitle -replace '^#+\s*', ''

    $projectRoot = if ($env:CLAUDE_PROJECT_DIR) { $env:CLAUDE_PROJECT_DIR } else { [string]$hookInput.cwd }
    $projectRoot = (Resolve-Path -LiteralPath $projectRoot).Path
    $referencesRoot = Join-Path $projectRoot 'references'
    $indexPath = Join-Path $projectRoot 'references.md'
    $entriesRoot = Join-Path $referencesRoot 'entries'

    if (-not (Test-Path -LiteralPath $referencesRoot)) {
        Write-HookContext "Reference-add request for '$requestedTitle': references/ does not exist. Do not create a record until the project reference structure is restored."
        exit 0
    }

    $requestedKey = Get-TitleKey $requestedTitle
    $fileExtensions = @('.pdf', '.txt', '.md')
    $candidatesByKey = @{}

    Get-ChildItem -LiteralPath $referencesRoot -Recurse -File |
        Where-Object { $fileExtensions -contains $_.Extension.ToLowerInvariant() } |
        ForEach-Object {
            $title = [System.IO.Path]::GetFileNameWithoutExtension($_.Name)
            $key = Get-TitleKey $title
            if ($key.Length -lt 5) {
                return
            }

            if (-not $candidatesByKey.ContainsKey($key)) {
                $candidatesByKey[$key] = [PSCustomObject]@{
                    Title = $title
                    Key   = $key
                    Paths = @()
                }
            }
            $candidatesByKey[$key].Paths += $_.FullName
        }

    $ranked = @(
        foreach ($candidate in $candidatesByKey.Values) {
            [PSCustomObject]@{
                Candidate = $candidate
                Score     = Get-TokenSimilarity -Left $requestedKey -Right $candidate.Key
            }
        }
    ) | Sort-Object -Property @{ Expression = 'Score'; Descending = $true }, @{ Expression = { $_.Candidate.Title }; Descending = $false }

    $topMatches = @($ranked | Select-Object -First 3)
    $selected = if ($topMatches.Count -gt 0 -and $topMatches[0].Score -ge 0.55) { $topMatches[0] } else { $null }

    if ($null -eq $selected) {
        $suggestions = if ($topMatches.Count -gt 0) {
            ($topMatches | ForEach-Object { "- $($_.Candidate.Title) (similarity $([math]::Round($_.Score * 100))%)" }) -join "`n"
        } else {
            '- No local reference files were found.'
        }

        Write-HookContext @"
Reference-add state report (generated locally)
Requested title: $requestedTitle
No local candidate reached the 55% title-similarity threshold.
Nearest local titles:
$suggestions

Required follow-up: treat these titles only as search hints. Locate and verify the requested paper's title, authors, year, and DOI/PMID from an authoritative record before creating any files. If an authorized original PDF is later placed in references/, run references/extract_pdf_text.py before completing the reference card. If extraction reports no text, mark OCR as required and do not invent an original-text citation. Do not modify introduce.md. Do not create a cited record, invent bibliographic data, or treat search1.md, search2.md, or search3.md as evidence.
"@
        exit 0
    }

    $candidate = $selected.Candidate
    $pdfPaths = @($candidate.Paths | Where-Object { [System.IO.Path]::GetExtension($_) -ieq '.pdf' })
    $sourceTextPaths = @($candidate.Paths | Where-Object {
        [System.IO.Path]::GetExtension($_) -ieq '.txt' -and
        [System.IO.Path]::GetFileNameWithoutExtension($_) -notmatch '번역|translation|translated' -and
        Test-NonEmptyText -Path $_
    })
    $translationPaths = @($candidate.Paths | Where-Object {
        $_ -match '논문_번역|번역|translation|translated'
    })
    $extractionMessages = @()

    if ($pdfPaths.Count -gt 0 -and $sourceTextPaths.Count -eq 0) {
        $pdfPath = $pdfPaths | Select-Object -First 1
        $extractorPath = Join-Path $projectRoot 'references\extract_pdf_text.py'
        $pythonPath = Join-Path $projectRoot '.venv\Scripts\python.exe'

        if (-not (Test-Path -LiteralPath $pythonPath)) {
            $pythonCommand = Get-Command python.exe -ErrorAction SilentlyContinue
            if ($null -ne $pythonCommand) {
                $pythonPath = $pythonCommand.Source
            }
        }

        if ((Test-Path -LiteralPath $extractorPath) -and (Test-Path -LiteralPath $pythonPath)) {
            $expectedTextPath = [System.IO.Path]::ChangeExtension($pdfPath, '.txt')
            try {
                $extractOutput = (& $pythonPath $extractorPath $pdfPath 2>&1 | Out-String).Trim()
                $extractExitCode = $LASTEXITCODE

                if ($extractExitCode -eq 0 -and (Test-NonEmptyText -Path $expectedTextPath)) {
                    $sourceTextPaths = @($expectedTextPath)
                    $extractionMessages += "Original text extraction: completed ($((Get-RelativePath -Path $expectedTextPath -ProjectRoot $projectRoot)))"
                    if ($extractOutput) {
                        $extractionMessages += "Extraction report:`n$extractOutput"
                    }
                } elseif ($extractExitCode -eq 0 -and (Test-Path -LiteralPath $expectedTextPath -PathType Leaf)) {
                    $extractionMessages += 'Original text extraction: completed, but no text was extracted; OCR may be required.'
                    if ($extractOutput) {
                        $extractionMessages += "Extraction report:`n$extractOutput"
                    }
                } else {
                    $extractionMessages += "Original text extraction: failed (exit code $extractExitCode)."
                    if ($extractOutput) {
                        $extractionMessages += "Extraction report:`n$extractOutput"
                    }
                }
            } catch {
                $extractionMessages += "Original text extraction: failed ($($_.Exception.Message))"
            }
        } else {
            $extractionMessages += 'Original text extraction: unavailable because the extractor or Python executable was not found.'
        }
    } elseif ($sourceTextPaths.Count -gt 0) {
        $extractionMessages += 'Original text extraction: skipped because a non-translation .txt already exists.'
    }

    $indexText = if (Test-Path -LiteralPath $indexPath) { Get-Content -LiteralPath $indexPath -Raw } else { '' }
    $registeredInIndex = $indexText.IndexOf($candidate.Title, [System.StringComparison]::OrdinalIgnoreCase) -ge 0

    $entryPaths = @()
    if (Test-Path -LiteralPath $entriesRoot) {
        $entryPaths = @(
            Get-ChildItem -LiteralPath $entriesRoot -File -Filter '*.md' | Where-Object {
                $entryText = Get-Content -LiteralPath $_.FullName -Raw
                $entryText.IndexOf($candidate.Title, [System.StringComparison]::OrdinalIgnoreCase) -ge 0
            } | Select-Object -ExpandProperty FullName
        )
    }

    $relativeFiles = @($candidate.Paths | ForEach-Object { Get-RelativePath -Path $_ -ProjectRoot $projectRoot } | Select-Object -First 8)
    $topTitles = ($topMatches | ForEach-Object { "- $($_.Candidate.Title) (similarity $([math]::Round($_.Score * 100))%)" }) -join "`n"
    $fileList = ($relativeFiles | ForEach-Object { "- $_" }) -join "`n"
    $pdfState = if ($pdfPaths.Count -gt 0) { "available ($($pdfPaths.Count))" } else { 'missing' }
    $textState = if ($sourceTextPaths.Count -gt 0) { "available ($($sourceTextPaths.Count))" } else { 'missing' }
    $translationState = if ($translationPaths.Count -gt 0) { "available ($($translationPaths.Count))" } else { 'missing' }
    $indexState = if ($registeredInIndex) { 'registered' } else { 'missing' }
    $entryState = if ($entryPaths.Count -gt 0) { "registered ($($entryPaths.Count))" } else { 'missing' }
    $extractionState = if ($extractionMessages.Count -gt 0) { $extractionMessages -join "`n" } else { 'Original text extraction: skipped because no source PDF was found.' }

    Write-HookContext @"
Reference-add state report (generated locally)
Requested title: $requestedTitle
Selected local candidate: $($candidate.Title) (similarity $([math]::Round($selected.Score * 100))%)
Other nearby titles:
$topTitles

Detected files:
$fileList
Original PDF: $pdfState
Non-translation original text (.txt): $textState
Translation file: $translationState
references.md index: $indexState
references/entries card: $entryState
$extractionState

Required follow-up: verify that the selected candidate and requested title are the same paper using title, authors, year, and DOI/PMID from the original text or another authoritative record. The Hook has attempted extraction whenever a local PDF existed and the original TXT was missing or empty. Use the extraction report above; if no text was extracted, mark OCR as required and do not invent quotations. Then create only the missing references.md index entry and references/entries card, using candidate status unless the paper is already cited in the thesis. If the identity cannot be verified or no original source is available, report the missing evidence instead of fabricating metadata. Do not modify introduce.md. Keep any generated translation in review-required status.
"@
} catch {
    Write-HookContext "Reference-add hook could not inspect the local reference state: $($_.Exception.Message). Continue with manual verification; do not make unverified reference changes."
}