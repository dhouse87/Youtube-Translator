@echo off
:: ==========================================
:: YouTube Translator - Batch Processing Tool
:: Instructions:
:: 1. Put your YouTube links in "input\links.txt"
::    (One link per line.)
:: 2. Double-click this file (run_translator.bat).
:: 3. Your outputs (transcripts and translations)
::    will be saved inside the "output\" folder.
::
:: Make sure Python is installed and added to PATH.
:: ==========================================

echo Launching YouTube Translator...

:: Move into the script directory
cd /d "%~dp0"

:: Create virtual folders if they don't exist
if not exist input mkdir input
if not exist output mkdir output

:: Check if input\links.txt exists
if not exist input\links.txt (
    echo ERROR: No "input\links.txt" file found!
    echo Please create one inside the "input" folder.
    pause
    exit /b
)

:: Run the Python translator program
python main.py

echo.
echo ==========================
echo Translation process done!
echo Check the "output" folder.
echo ==========================
pause
