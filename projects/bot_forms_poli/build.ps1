$exclude = @("venv", "bot_forms_poli.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_forms_poli.zip" -Force