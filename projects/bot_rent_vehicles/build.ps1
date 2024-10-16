$exclude = @("venv", "bot_rent_vehicles.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_rent_vehicles.zip" -Force