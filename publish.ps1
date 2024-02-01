param (
    [string]$commitTitle
)

git add .

$originalLocation = Get-Location
$articlesFolder = "./articles/"
$githubRepoURL = "https://raw.githubusercontent.com/MaciekWin3/blog/main"

function ReplaceImagePaths($file) {
    $content = Get-Content $file -Raw
    $fits = $content | Select-String '!\[image\]\(./assets/(.+?)\)' -AllMatches | ForEach-Object { $_.Matches }
    
    foreach ($match in $fits) {
        $oldPath = $match.Groups[0].Value
        $newPath = '<p align="center"><img src="' + $githubRepoURL + '/articles/assets/' + $match.Groups[1].Value + '" alt="Custom image"/></p>'
        $content = $content -replace [regex]::Escape($oldPath), $newPath
    }

    Set-Content -Path $file -Value $content
}

Set-Location -Path $articlesFolder
$markdownFiles = Get-ChildItem -Filter *.md
foreach ($file in $markdownFiles) {
    ReplaceImagePaths $file.FullName
}

Set-Location -Path $originalLocation

git add . 
git commit -m $commitTitle
git push
