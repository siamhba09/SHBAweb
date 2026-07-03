@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ========================================
echo   Push SHBA project to GitHub
echo ========================================
echo.

REM เคลียร์ lock file ที่ค้าง (ถ้ามี)
if exist ".git\index.lock" (
    echo Removing stale index.lock ...
    del /f /q ".git\index.lock"
)

echo Current changes:
git status -s
echo.

set /p MSG="Commit message (Enter = ใช้ค่า default): "
if "%MSG%"=="" set MSG=Update website content and assets

echo.
echo Staging all changes ...
git add -A

echo Committing ...
git commit -m "%MSG%"

echo.
echo Pushing to origin/main ...
git push origin main

echo.
if %ERRORLEVEL%==0 (
    echo ========================================
    echo   Done! อัพขึ้น GitHub เรียบร้อยแล้ว
    echo ========================================
) else (
    echo ========================================
    echo   Push failed - เช็คการ login GitHub
    echo   ให้แน่ใจว่าติดตั้ง Git Credential Manager
    echo   หรือ login GitHub ไว้แล้ว
    echo ========================================
)
echo.
pause
