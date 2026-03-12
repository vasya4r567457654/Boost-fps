import tkinter as tk
from tkinter import messagebox
import os
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def real_boost():
    if not is_admin():
        messagebox.showwarning("Ошибка", "Запусти IDLE или файл от имени администратора!")
        return

    try:
        # 1. Снижение пинга (отключаем ограничение сети)
        os.system('reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "NetworkThrottlingIndex" /t REG_DWORD /d 0xffffffff /f')
        
        # 2. Максимальный приоритет для игр
        os.system('reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "SystemResponsiveness" /t REG_DWORD /d 0 /f')
        
        # 3. Очистка DNS кэша
        os.system("ipconfig /flushdns")
        
        # 4. Включение схемы питания "Максимальная производительность"
        os.system("powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")
        
        messagebox.showinfo("Успех", "Настройки применены!\n1. Пинг оптимизирован\n2. Питание на максимум\n3. DNS очищен")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Что-то пошло не так: {e}")

# Интерфейс
root = tk.Tk()
root.title("PRO Game Booster")
root.geometry("350x250")
root.configure(bg="#121212")

label = tk.Label(root, text="SYSTEM OPTIMIZER", fg="#00ff00", bg="#121212", font=("Courier", 16, "bold"))
label.pack(pady=20)

btn = tk.Button(root, text="RUN REAL BOOST", command=real_boost, 
               bg="#00ff00", fg="black", font=("Arial", 12, "bold"), 
               padx=20, pady=10)
btn.pack(pady=20)

root.mainloop()
