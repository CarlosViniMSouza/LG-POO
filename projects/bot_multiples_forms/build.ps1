$exclude = @("venv", "bot_multiples_forms.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_multiples_forms.zip" -Force