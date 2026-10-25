$ErrorActionPreference = 'Stop'

$references = Split-Path -Parent $PSScriptRoot
$destination = Join-Path $references 'crossfit'

$files = @(
    'Comparison of the effects of different physical activities on laterality and asymmetry values through side bridge test.pdf',
    'Comparison of the effects of different physical activities on laterality and asymmetry values through side bridge test.txt',
    'CrossFit vs. sedentary lifestyle unveiling the effects on strength, balance and quality of life.pdf',
    'CrossFit vs. sedentary lifestyle unveiling the effects on strength, balance and quality of life.txt',
    'MedXFit—Effects of 6 months CrossFit in sedentary and inactive employees A prospective, controlled, longitudinal, intervention study.pdf',
    'MedXFit—Effects of 6 months CrossFit in sedentary and inactive employees A prospective, controlled, longitudinal, intervention study.txt'
)

foreach ($file in $files) {
    $source = Join-Path $references $file
    if (Test-Path -LiteralPath $source) {
        Move-Item -LiteralPath $source -Destination $destination
    }
}
