$exclude = @("venv", "bot_store_files.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_store_files.zip" -Force