$Env:PATH = Read-Host "Enter Maltego path"

$Env:MPSIEM_URL = Read-Host "Enter mpsiem URL without https://"

$Env:MPSIEM_LOGIN = Read-Host "Enter MPSIEM login"

$Env:MPSIEM_PASSWORD = Read-Host "Enter MPSIEM password"

maltego

Read-Host -Prompt "Either Maltego was closed or the path to the executable was incorrect"