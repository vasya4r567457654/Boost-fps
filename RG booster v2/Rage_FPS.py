import os
import sys
import ctypes
import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk
import time
import winsound
import threading

def resource_path(relative_path):
    try: base_path = sys._MEIPASS
    except Exception: base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def is_admin():
    try: return ctypes.windll.shell32.IsUserAnAdmin()
    except: return False

def activate_ultra_boost(log_widget):
    if not is_admin():
        messagebox.showwarning("Доступ", "Запусти от имени администратора!")
        return

    log_widget.insert(tk.END, ">>> ЗАПУСК УЛЬТРА-УСКОРЕНИЯ (ЦЕЛЬ: MAX MBIT)...\n", "info")
    
    try:
        # 1. СНЯТИЕ ОГРАНИЧЕНИЙ WINDOWS (ТВОЯ БАЗА + НОВОЕ)
        log_widget.insert(tk.END, "> Снятие лимитов пропускной способности...\n")
        os.system('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Psched" /v "NonBestEffortLimit" /t REG_DWORD /d 0 /f')
        os.system('reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "NetworkThrottlingIndex" /t REG_DWORD /d 4294967295 /f')
        
        # 2. РАЗГОН TCP-СТЕКА ДЛЯ ВЫСОКИХ СКОРОСТЕЙ
        log_widget.insert(tk.END, "> Оптимизация алгоритма передачи данных...\n")
        os.system('netsh int tcp set global autotuninglevel=experimental')
        os.system('netsh int tcp set global congestionprovider=ctcp')
        os.system('netsh int tcp set global rss=enabled')
        os.system('netsh int tcp set global fastopen=enabled')

        # 3. МАКСИМАЛЬНОЕ СНИЖЕНИЕ ПИНГА
        log_widget.insert(tk.END, "> Настройка мгновенного отклика...\n")
        os.system('reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "TcpAckFrequency" /t REG_DWORD /d 1 /f')
        os.system('reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "TCPNoDelay" /t REG_DWORD /d 1 /f')
        
        # 4. СТАБИЛИЗАЦИЯ И FPS
        log_widget.insert(tk.END, "> Стабилизация FPS и питания...\n")
        os.system('powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c')
        os.system('reg add "HKCU\System\GameConfigStore" /v "GameDVR_Enabled" /t REG_DWORD /d 0 /f')

        # 5. ОБНОВЛЕНИЕ БЕЗ РАЗРЫВА
        log_widget.insert(tk.END, "> Очистка сетевого мусора...\n")
        os.system('ipconfig /flushdns >nul')
        os.system('netsh winsock reset catalog >nul')

        log_widget.insert(tk.END, ">>> МАКСИМАЛЬНЫЙ РЕЖИМ ВКЛЮЧЕН!\n", "success")
        winsound.Beep(1200, 500)
        messagebox.showinfo("Rage_FPS Ultra", "Лимиты сняты! Теперь скорость должна пробить 45 Мбит/с.")

    except Exception as e:
        log_widget.insert(tk.END, f"!! Ошибка: {e}\n", "error")

# --- ГРАФИКА ---
root = tk.Tk()
root.title("RAGE FPS | ULTRA SPEED")
root.geometry("500x750")
root.configure(bg="#050505")

photo_frame = tk.Frame(root, bg="#00ffcc", bd=1)
photo_frame.pack(pady=20)

try:
    path = resource_path("my_photo.jpg")
    img = Image.open(path).resize((220, 260), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    tk.Label(photo_frame, image=photo, bg="#050505").pack(padx=2, pady=2)
except:
    tk.Label(photo_frame, text="MAX PERFORMANCE", fg="#00ffcc", bg="#050505", width=25, height=10).pack()

tk.Label(root, text="RAGE FPS v1.5 ULTRA", fg="#00ffcc", bg="#050505", font=("Impact", 24)).pack()

log_area = scrolledtext.ScrolledText(root, bg="#0a0a0a", fg="#00ffcc", font=("Consolas", 10), height=12)
log_area.pack(fill="both", padx=20, pady=10)
log_area.tag_config("success", foreground="#00ff00")
log_area.tag_config("info", foreground="#00ccff")

def start():
    threading.Thread(target=activate_ultra_boost, args=(log_area,), daemon=True).start()

tk.Button(root, text="ACTIVATE ULTRA SPEED", command=start, 
          bg="#00ffcc", fg="black", font=("Arial Black", 12), relief="flat", height=2).pack(pady=20, fill="x", padx=40)

root.mainloop()
