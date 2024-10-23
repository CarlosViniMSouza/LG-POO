$exclude = @("venv", "bot_payment_employeer.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_payment_employeer.zip" -Force