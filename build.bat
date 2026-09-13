@echo off
setlocal

rem Rebuilds dist\BedroomLighting.exe from the current source and syncs the
rem scenes and .env next to it, since the taskbar shortcut runs that exe
rem directly and won't pick up source/scene changes until this is run.

cd /d "%~dp0"

echo Building BedroomLighting.exe...
".venv\Scripts\python.exe" -m PyInstaller app.spec --noconfirm
if errorlevel 1 (
    echo Build failed - see errors above.
    exit /b 1
)

echo Syncing scenes and .env into dist...
if not exist "dist\scenes" mkdir "dist\scenes"
if exist "dist\scenes\__pycache__" rmdir /s /q "dist\scenes\__pycache__"
xcopy /y /i "scenes\*.json" "dist\scenes\" >nul
copy /y ".env" "dist\.env" >nul

echo.
echo Done. dist\BedroomLighting.exe is up to date.

endlocal
