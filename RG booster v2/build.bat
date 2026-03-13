@echo off
cd /d "D:\RG booster"
rd /s /q build dist 2>nul
echo [1/2] Сборка проекта...
:: Добавляем все возможные варианты фото, если они есть
python -m PyInstaller --noconsole --onefile --uac-admin --add-data "my_photo*;." Rage_FPS.py
if exist dist\Rage_FPS.exe (
    echo [2/2] УСПЕХ!
    start dist
) else (
    echo ОШИБКА СБОРКИ!
)
pause