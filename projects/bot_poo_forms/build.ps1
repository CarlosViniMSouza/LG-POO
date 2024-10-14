$exclude = @("venv", "bot_poo_forms.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_poo_forms.zip" -Force