@echo off

START taskmgr.exe
START cmd.exe

cd "C:\Users\WDAGUtilityAccount\setup"
"AutoHotkey_1.1.35.00_setup.exe" /S

curl -L "https://update.code.visualstudio.com/latest/win32-x64-user/stable" --output "C:\Users\WDAGUtilityAccount\Downloads\vscode-silent.exe"
"C:\Users\WDAGUtilityAccount\Downloads\vscode-silent.exe" /silent

"python-3.11.0-amd64.exe" /passive PrependPath=1 Include_pip=1 InstallAllUsers=1

echo DOne