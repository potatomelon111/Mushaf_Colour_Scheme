# PowerShell to convert all SVGs in folder to individual PDFs using Inkscape
$inputFolder = "C:\Users\path\to\SVGs"
$outputFolder = "C:\Users\path\to\PDF_folder"
New-Item -ItemType Directory -Force -Path $outputFolder

Get-ChildItem -Path $inputFolder -Filter *.svg | ForEach-Object {
    $infile = $_.FullName
    $outfile = Join-Path $outputFolder ($_.BaseName + ".pdf")
    & "C:\Program Files\Inkscape\bin\inkscape.com" $infile --export-type=pdf --export-filename=$outfile
}
