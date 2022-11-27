::https://github.com/Cornelius-Figgle/ROSA/
::ROBOTICALLY OBNOXIOUS SERVING ASSISTANT

::THIS FILE IS PART OF THE `ROSA` REPO, MAINTAINED AND PRODUCED BY MAX HARRISON, AS OF 2022
::It may work separately and independently, it may not
::
::Code (c) Max Harrison 2022
::Ideas (c) Callum Blumfield 2022
::Ideas (c) Max Harrison 2022
::Vocals (c) Evie Peacock 2022
::
::Thanks also to Alex, Ashe & Jake for support throughout (sorry for the spam)
::also thanks to all the internet peoples that helped with this as well 



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

:: set exe=^"%1^"
:: set lnk=^"%2^"
:: set ico=^"%3^"
:: set text=^"%4^"

set exe=%1
set work=%~dp1
set lnk=%2
set ico=%3
set text=%4

cd %exe%

echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = %lnk% >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = %exe% >> CreateShortcut.vbs
echo oLink.WorkingDirectory = %work% >> CreateShortcut.vbs
echo oLink.Description = %text% >> CreateShortcut.vbs
echo oLink.IconLocation = %ico% >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs

cscript CreateShortcut.vbs