@echo off
chcp 65001 > nul
title YouTube Downloader - تشغيل مباشر

echo.
echo =========================================================
echo           [ Youtube Downloader - تشغيل مباشر ]
echo =========================================================
echo.

:menu
echo 1. تحميل فيديو (أفضل جودة)
echo 2. تحميل صوت فقط
echo 3. تحميل بجودة محددة
echo 4. الخروج
echo.
set /p choice=   اختر رقم: 

if "%choice%"=="1" goto best
if "%choice%"=="2" goto audio
if "%choice%"=="3" goto custom
if "%choice%"=="4" exit

:best
echo.
set /p url=   أدخل رابط YouTube: 
yt-dlp -f "bestvideo+bestaudio/best" --merge-output-format mp4 "%url%"
goto end

:audio
echo.
set /p url=   أدخل رابط YouTube: 
yt-dlp -x --audio-format mp3 "%url%"
goto end

:custom
echo.
set /p url=   أدخل رابط YouTube: 
echo   أمثلة: 720p => 'best[height<=720]', 1080p => 'best[height<=1080]'
set /p quality=   أدخل الجودة المطلوبة: 
yt-dlp -f "%quality%" "%url%"
goto end

:end
echo.
echo   التحميل اكتمل!
echo.
pause
goto menu