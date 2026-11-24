@echo off
setlocal

cd /d D:\Automation\SAP-Stock-Export

if not exist ".venv\Scripts\python.exe" (
    echo [ERROR] Virtual environment tidak ditemukan.
    pause
    exit /b 1
)

call ".venv\Scripts\activate.bat"

echo.
echo ========================================
echo SAP STOCK EXPORT
echo ========================================
echo.

echo Membuka SAP Logon...

start "" "C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"

echo.
echo SAP Logon sudah dijalankan.
echo.
pause