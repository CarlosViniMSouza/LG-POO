$exclude = @("venv", "bot_bookstore.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_bookstore.zip" -Force