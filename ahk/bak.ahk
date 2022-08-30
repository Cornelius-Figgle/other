#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

Menu,Tray,Icon,%A_ScriptDir%\icons\loading.ico,,0
#KeyHistory 0
#SingleInstance On


^#s::
    Tooltip, bak
    DriveGet, fixedDrives, List, FIXED
    If (ErrorLevel != 0)
        reportError() 

    If fixedDrives contains F 
    {
        FileRemoveDir, f:\__pcBak\COD3\bak\*, 1
        If (ErrorLevel != 0)
            reportError()

        FormatTime, isoCurrentTime, A_NowUTC, yyyyMMddTHHmmssZ
        bakPath = f:\__pcBak\COD3\bak\%isoCurrentTime%\source
        If (ErrorLevel != 0)
            reportError() 

        FileMoveDir, f:\__pcBak\COD3\source, %bakPath%, 2
        If (ErrorLevel != 0)
            reportError() 


        FileCopyDir, c:\users\max.harrison\source, f:\__pcBak\COD3\source, 1
        If (ErrorLevel != 0)
            reportError() 
        
        FormatTime, isoCurrentTime, A_NowUTC, yyyyMMddTHHmmssZ
        FileAppend, %isoCurrentTime% | Ln: %A_LineNumber% | 'Bak 2 F:\ Complete'`n, c:\users\max.harrison\source\ahk\logs\bak\logs.txt
    }
    FormatTime, isoCurrentTime, A_NowUTC, yyyyMMddTHHmmssZ
    FileAppend, %isoCurrentTime% | Ln: %A_LineNumber% | `n, c:\users\max.harrison\source\ahk\logs\bak\logs.txt
    Tooltip

Return

reportError() 
{
    MsgBox, 0, bak, Ln: %A_LineNumber% | ErLvl: %ErrorLevel% | LastEr: %A_LastError%, 5
    FormatTime, isoCurrentTime, A_NowUTC, yyyyMMddTHHmmssZ
    FileAppend, %isoCurrentTime% | Ln: %A_LineNumber% | ErLvl: %ErrorLevel% | LastEr: %A_LastError%, c:\users\max.harrison\source\ahk\logs\bak\logs.txt
}