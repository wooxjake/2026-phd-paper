Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$projectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..\..')).Path
$pythonPath = Join-Path $projectRoot '.venv\Scripts\python.exe'
$scriptPath = Join-Path $projectRoot '.github\hooks\add-reference-copilot.py'

if (-not (Test-Path -LiteralPath $pythonPath)) {
    $pythonCommand = Get-Command python.exe -ErrorAction SilentlyContinue
    if ($null -ne $pythonCommand) {
        $pythonPath = $pythonCommand.Source
    }
}

if (-not (Test-Path -LiteralPath $pythonPath)) {
    @{ continue = $true; systemMessage = 'Copilot /add Hook could not find a Python executable.' } |
        ConvertTo-Json -Compress
    exit 0
}

$hookInput = [Console]::In.ReadToEnd()
$hookInput | & $pythonPath $scriptPath
exit $LASTEXITCODE
