$Env:PATH = Read-Host "Enter Maltego path"

$Env:MPSIEM_URL = Read-Host "Enter mpsiem URL without https://"

$credential = Get-Credential

$Env:MPSIEM_LOGIN = $credential.GetNetworkCredential().username

$Env:MPSIEM_PASSWORD = $credential.GetNetworkCredential().password

maltego

Read-Host -Prompt "Either Maltego was closed or the path to the executable was incorrect"