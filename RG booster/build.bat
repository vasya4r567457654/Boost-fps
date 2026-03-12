@echo off
:: Переходим на диск D
d:
:: Заходим в папку со скриптом (если папка называется MyProject)
cd "D:\MyProject"

echo Starting PyInstaller...
"C:\Program Files\Python313\python.exe" -m PyInstaller --onefile --noconsole --uac-admin "Rage_FPS.py"

echo.
echo Process finished! Check the 'dist' folder.
pause