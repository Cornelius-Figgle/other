:: %0 is sys call of batch file
:: %1 is full path of exe
:: %2 is full path of lnk
:: %3 is full path of ico
:: %4 is shortcut text

:: https://stackoverflow.com/a/35050564/19860022
:: https://superuser.com/questions/455364/how-to-create-a-shortcut-using-a-batch-script

@echo off

set argC=0
for %%x in (%*) do Set /A argC+=1 && echo %%x
echo N* of Args: %argC% 

set exe=^"%1^"
set lnk=^"%2^"
set ico=^"%3^"
set text=%4

echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = %lnk% >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = %exe% >> CreateShortcut.vbs
echo oLink.WorkingDirectory = %exe% >> CreateShortcut.vbs
echo oLink.Description = %text% >> CreateShortcut.vbs
echo oLink.IconLocation = %ico% >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs

cscript CreateShortcut.vbs
del CreateShortcut.vbs