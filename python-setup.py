import os import subprocess import sys import threading import customtkinter as ctk from tkinter import messagebox from pathlib import Path

Cấu hình giao diện

ctk.set_appearance_mode("System") ctk.set_default_color_theme("blue")

class PythonInstallerApp(ctk.CTk): def init(self): super().init() self.title("Python & Libraries Installer") self.geometry("500x400") self.resizable(False, False)

# Giao diện
    self.label = ctk.CTkLabel(self, text="Cài đặt Python (nếu cần) và các thư viện", font=ctk.CTkFont(size=16))
    self.label.pack(pady=20)

    self.button = ctk.CTkButton(self, text="Bắt đầu cài đặt", command=self.start_installation)
    self.button.pack(pady=10)

    self.logbox = ctk.CTkTextbox(self, width=460, height=260)
    self.logbox.pack(pady=10)
    self.log("Sẵn sàng.\n")

def log(self, text: str):
    self.logbox.insert("end", text + "\n")
    self.logbox.see("end")
    print(text)

def run_cmd(self, cmd, shell=False):
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=shell)
        for line in proc.stdout:
            self.log(line.strip())
        proc.wait()
        return proc.returncode == 0
    except Exception as e:
        self.log(f"[Lỗi] {e}")
        return False

def is_python_installed(self):
    try:
        output = subprocess.check_output(["python", "--version"], stderr=subprocess.STDOUT, text=True)
        self.log("Phát hiện Python: " + output.strip())
        return True
    except:
        return False

def install_python(self):
    setup_path = os.path.join(os.getcwd(), "python-setup.exe")
    if not os.path.exists(setup_path):
        self.log("[Lỗi] Không tìm thấy file: python-setup.exe")
        messagebox.showerror("Lỗi", "Không tìm thấy python-setup.exe trong thư mục hiện tại.")
        return False

    self.log("Đang cài đặt Python...")
    return self.run_cmd([
        setup_path,
        "/quiet",
        "InstallAllUsers=1",
        "PrependPath=1",
        "Include_pip=1"
    ], shell=True)

def install_packages(self):
    packages = ["customtkinter", "yt_dlp", "Pillow", "requests"]
    for pkg in packages:
        self.log(f"Đang cài {pkg}...")
        ok = self.run_cmd(["python", "-m", "pip", "install", "--upgrade", pkg])
        if not ok:
            self.log(f"[Lỗi] Không thể cài {pkg}")
            return False
    return True

def installation_process(self):
    self.button.configure(state="disabled")

    # Bước 1: Cài Python nếu chưa có
    if not self.is_python_installed():
        self.log("Chưa có Python. Bắt đầu cài đặt...")
        if not self.install_python():
            self.log("[Lỗi] Cài đặt Python thất bại.")
            messagebox.showerror("Lỗi", "Cài đặt Python thất bại.")
            self.button.configure(state="normal")
            return
        self.log("Đã cài đặt Python. Khởi động lại ứng dụng để tiếp tục.")
        messagebox.showinfo("Thông báo", "Đã cài xong Python. Hãy đóng và chạy lại ứng dụng.")
        sys.exit(0)

    # Bước 2: Cài thư viện pip
    self.log("Cài đặt các thư viện pip...")
    if self.install_packages():
        self.log("Hoàn tất! Python và các thư viện đã được cài.")
        messagebox.showinfo("Thành công", "Đã cài đặt Python và các thư viện.")
        sys.exit(0)
    else:
        messagebox.showerror("Lỗi", "Cài đặt một số thư viện thất bại.")

    self.button.configure(state="normal")

def start_installation(self):
    threading.Thread(target=self.installation_process, daemon=True).start()

if name == "main": app = PythonInstallerApp() app.mainloop()

