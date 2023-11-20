@echo off
set WINSCP_PATH="C:\Program Files (x86)\WinSCP\WinSCP.com"
set FTP_HOST=nas.webzen.co.kr
set FTP_PORT=23145
set FTP_USER=mssung@webzen.com
set FTP_PASSWORD=webzen@2311
set LOCAL_PATH=D:\R2A
set LOCAL_PATH_DATA=D:\R2A\data
set FTP_PATH=/R2A

%WINSCP_PATH% /log=upload.log /command ^
    "open ftp://%FTP_USER%:%FTP_PASSWORD%@%FTP_HOST%:%FTP_PORT%" ^
    "cd %FTP_PATH%" ^
    "lcd %LOCAL_PATH%" ^
    "put -neweronly log" ^
    "exit"

