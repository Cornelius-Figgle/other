#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

Menu,Tray,Icon,%A_ScriptDir%\icons\loading.ico,,0
#KeyHistory 0
#SingleInstance On


^#s::
    Tooltip, bak
    DriveGet, fixedDrives, List, FIXED 

    If fixedDrives contains F 
    {
        FileRemoveDir, f:\__pcBak\COD3\bak, 1

        FormatTime, isoCurrentTime, A_NowUTC, yyyyMMddTHHmmssZ
        bakPath = f:\__pcBak\COD3\bak\%isoCurrentTime%\source

        FileMoveDir, f:\__pcBak\COD3\source, %bakPath%, 2


        FileCopyDir, t:\, f:\__pcBak\COD3\source, 1
    }
    Tooltip

Return