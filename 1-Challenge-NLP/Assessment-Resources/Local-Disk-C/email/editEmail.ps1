$labVariables = Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Virtual Machine\External"
$rg = Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Virtual Machine\External" -Name "*cloudresourcegroup*1*name" | Select-Object -ExpandProperty "*cloudresourcegroup*1*name"
$labInstanceID = $labVariables.'@lab.LabInstance.Id'

$hashTable = @{
	'User-@labinstanceid' = $labVariables.'@lab.CloudPortalCredential(1).Username'
	'password-@labinstanceid' = $labVariables.'@lab.CloudPortalCredential(1).Password'
	"User1-@labinstanceid" = "User1-$labInstanceID"
	'rg-@labinstanceid' = $rg 
	'RG2@labinstanceID' = $labVariables.'@lab.CloudResourceGroup(2).Name'
	'app1sa@labinstanceid' = "app1sa$labInstanceID"
	'app2sa@labinstanceid' = "app2sa$labInstanceID"
	'data@labinstanceid' = "data$labInstanceID"
	'replica@labinstanceid' = "replica$labInstanceID"
	'Project2-KV@labinstanceid' = "Project2-KV$labInstanceID"
	'prototype@labinstanceid' = "prototype$labInstanceID"
	'qualityassurance@labinstanceid' = "qualityassurance$labInstanceID"
	'form@labinstanceid' = "form$labInstanceID"
	'kv@labinstanceid' = "kv$labInstanceID"
	'sqlserver@labinstanceid' = "sqlserver$labInstanceID"
    'sa@labinstanceid' = "sa$labInstanceID"
	'lang-@labinstanceid' = "lang-$labInstanceID"
	'sqldbserver-@labinstanceid' = "sqldbserver-$labInstanceID"
	'@labinstanceid-DBA' = "$labinstanceid-DBA"
	'acr@labinstanceid' = "acr$labinstanceid"
	'@labinstanceid-AppLogExaminers' = "$labinstanceid-AppLogExaminers"
	'AzureWebApp1-@labinstanceid' = "AzureWebApp1-$labinstanceid"
	'acrid@labinstanceid' = "acrid$labinstanceid"
	'admin@labinstanceid' = "admin$labinstanceid"
	'cs1-@labinstanceid' = "cs1-$labinstanceid"
	'azureml@labinstanceid' = "azureml$labinstanceid"
	'todoapi-@labinstanceid' = "todoapi-$labinstanceid"
	'WebApp1-@labinstanceid' = "WebApp1-$labinstanceid"
	'Operator1-@labinstanceid' = "Operator1-$labInstanceID"
	'bus@labinstanceid' = "bus$labInstanceID"
	'@azureMLworkspacename' = "azuremlworkspace$labInstanceID"
	'search@labinstanceid' = "search$labInstanceID"
}

if (Test-Path C:\email\email.html) {
    foreach ($key in $hashTable.GetEnumerator()){
        $content = Get-Content C:\email\email.html
        $content.Replace($key.Name, $key.Value) | Set-Content C:\email\email.html
    }
}