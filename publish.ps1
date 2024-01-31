param (
    [string]$commitTitle
)

# Add changes to git
git add .

# Record the current location
$originalLocation = Get-Location

# Path to the articles folder
$articlesFolder = "./articles/"

# GitHub repo URL (raw content)
$githubRepoURL = "https://raw.githubusercontent.com/MaciekWin3/blog/main"

# Function to replace local image paths with GitHub repo paths
function ReplaceImagePaths($file) {
    $content = Get-Content $file -Raw
    $content = $content -replace '!\[image\]\(./assets/', "![image]($githubRepoURL/articles/assets/"
    Set-Content -Path $file -Value $content
}

# Change to the articles folder
Set-Location -Path $articlesFolder

# Get all markdown files in the folder
$markdownFiles = Get-ChildItem -Filter *.md

# Loop through each markdown file
foreach ($file in $markdownFiles) {
    # Replace local image paths with GitHub repo paths
    ReplaceImagePaths $file.FullName
}

# Add changes to git
git add .

# Commit changes with the specified title
git commit -m $commitTitle

# Push changes to GitHub
git push

# Return to the original location
Set-Location -Path $originalLocation
