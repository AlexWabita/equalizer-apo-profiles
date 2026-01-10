@echo off
REM ================================================================
REM AUTO PROFILE SWITCHER BY TIME OF DAY
REM ================================================================
REM This script automatically switches EQ profiles based on time
REM 
REM SETUP:
REM 1. Edit the time ranges and profile paths below
REM 2. Save this file to: C:\Scripts\auto_eq_switch.bat
REM 3. Create a Windows Task Scheduler task to run this hourly
REM 
REM TASK SCHEDULER SETUP:
REM 1. Open Task Scheduler
REM 2. Create Basic Task
REM 3. Name: "Auto EQ Profile Switcher"
REM 4. Trigger: Daily, repeat every 1 hour
REM 5. Action: Start a program
REM 6. Program: C:\Scripts\auto_eq_switch.bat
REM 7. Start in: C:\Scripts\
REM ================================================================

REM Get current hour (24-hour format)
for /f "tokens=1-2 delims=:" %%a in ('time /t') do (
    set hour=%%a
)

REM Remove leading zero if present
if "%hour:~0,1%"=="0" set hour=%hour:~1,1%

REM Define config file path
set CONFIG_PATH=C:\Program Files\EqualizerAPO\config\config.txt

REM ================================================================
REM TIME-BASED PROFILE SELECTION
REM ================================================================
REM Customize these time ranges and profiles to your preference

REM LATE NIGHT / EARLY MORNING (12 AM - 6 AM)
if %hour% GEQ 0 if %hour% LSS 6 (
    echo ^Include: occasions/config_night.txt > "%CONFIG_PATH%"
    echo [%date% %time%] Switched to Night Mode
    goto :end
)

REM MORNING (6 AM - 9 AM)
if %hour% GEQ 6 if %hour% LSS 9 (
    echo ^Include: occasions/config_morning.txt > "%CONFIG_PATH%"
    echo [%date% %time%] Switched to Morning Mode
    goto :end
)

REM WORK HOURS (9 AM - 12 PM)
if %hour% GEQ 9 if %hour% LSS 12 (
    echo ^Include: occasions/config_balanced.txt > "%CONFIG_PATH%"
    echo [%date% %time%] Switched to Balanced Mode
    goto :end
)

REM AFTERNOON (12 PM - 5 PM)
if %hour% GEQ 12 if %hour% LSS 17 (
    echo ^Include: occasions/config_balanced.txt > "%CONFIG_PATH%"
    echo [%date% %time%] Switched to Balanced Mode
    goto :end
)

REM EARLY EVENING (5 PM - 8 PM)
if %hour% GEQ 17 if %hour% LSS 20 (
    echo ^Include: occasions/config_romantic.txt > "%CONFIG_PATH%"
    echo [%date% %time%] Switched to Romantic Mode
    goto :end
)

REM LATE EVENING (8 PM - 10 PM)
if %hour% GEQ 20 if %hour% LSS 22 (
    echo ^Include: occasions/config_party.txt > "%CONFIG_PATH%"
    echo [%date% %time%] Switched to Party Mode
    goto :end
)

REM NIGHT TIME (10 PM - 12 AM)
if %hour% GEQ 22 if %hour% LSS 24 (
    echo ^Include: occasions/config_night.txt > "%CONFIG_PATH%"
    echo [%date% %time%] Switched to Night Mode
    goto :end
)

:end
REM ================================================================
REM RELOAD EQUALIZER APO CONFIGURATION
REM ================================================================
REM This forces Equalizer APO to reload the new configuration
REM Note: Requires restart of audio service or application

REM Uncomment ONE of the following methods:

REM Method 1: Restart Windows Audio service (requires admin)
REM net stop audiosrv
REM net start audiosrv

REM Method 2: Kill and restart Configuration Editor (if running)
REM taskkill /F /IM Editor.exe
REM start "" "C:\Program Files\EqualizerAPO\Editor\Editor.exe"

REM Method 3: Touch the config file (triggers reload in some setups)
copy /b "%CONFIG_PATH%"+,, "%CONFIG_PATH%"

echo Profile switch complete!
exit /b 0


REM ================================================================
REM CUSTOMIZATION IDEAS
REM ================================================================
REM
REM 1. WEEKEND VS WEEKDAY:
REM    Add day-of-week detection for different weekend schedules
REM
REM 2. ACTIVITY-BASED:
REM    Combine with other scripts to detect running applications
REM    (e.g., gaming, video player, music app)
REM
REM 3. LOCATION-BASED:
REM    Check WiFi network to use different profiles at home vs work
REM
REM 4. LOGGING:
REM    Add logging to track profile switches
REM    echo [%date% %time%] Switched to X >> C:\Scripts\eq_log.txt
REM
REM 5. MANUAL OVERRIDE:
REM    Create a flag file to temporarily disable auto-switching
REM    if exist C:\Scripts\eq_manual.flag goto :end
REM
REM ================================================================


REM ================================================================
REM TROUBLESHOOTING
REM ================================================================
REM
REM Q: Script not running?
REM A: Check Task Scheduler is enabled and task is set to run
REM
REM Q: Profiles not switching?
REM A: Verify paths are correct, check file permissions
REM
REM Q: Need to test manually?
REM A: Run this .bat file directly by double-clicking it
REM
REM Q: Want to see what time it is?
REM A: Add "echo Current hour: %hour%" before the if statements
REM
REM ================================================================