# python-setup

**Compile to EXE for automatic Python installation and library setup.**

Source code: [https://github.com/nguyenhhoa03/python-setup](https://github.com/nguyenhhoa03/python-setup)

---

## Mô tả

`python-setup` là một ứng dụng GUI viết bằng Python và [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) giúp:

1. Tạo file thực thi `.exe` để tự động kiểm tra và cài đặt Python trên Windows.
2. Cài Python (nếu chưa có) từ file `python-setup.exe` (nằm cùng thư mục).
3. Tự động thiết lập môi trường với các thư viện cần thiết:
   - `customtkinter`
   - `yt_dlp`
   - `Pillow`
   - `requests`
4. Hiển thị log chi tiết quá trình cài đặt và thông báo kết quả.

---

## Tính năng

- Biên dịch thành file `.exe`, không yêu cầu Python có sẵn trên máy.
- Cài đặt Python im lặng với các tham số:
  - `/quiet`
  - `InstallAllUsers=1`
  - `PrependPath=1`
  - `Include_pip=1`
- Tự động cài và nâng cấp các thư viện pip thiết yếu.
- Giao diện thân thiện, dễ sử dụng với CustomTkinter.
- Log tiến trình chi tiết ngay trên GUI.

---

## Yêu cầu

- Hệ điều hành: Windows 7 trở lên.
- File `python-setup.exe` (installer chính thức của Python) phải nằm cùng thư mục với file `.exe` của ứng dụng.

---

## Cài đặt

1. Clone hoặc tải project về:
   ```bash
   git clone https://github.com/nguyenhhoa03/python-setup.git
   cd python-setup```

2. Đặt file cài đặt Python (Windows installer) vào thư mục project và đổi tên thành `python-setup.exe`.

---

## Hướng dẫn sử dụng

1. Biên dịch ứng dụng thành `.exe` (lần đầu cần Python để biên dịch):

   ```bash
   pip install pyinstaller
   pyinstaller --onefile python_installer_gui.py
   ```
2. Sau khi có file `python_installer_gui.exe`, chạy trực tiếp trên Windows.
3. Giao diện sẽ tự động kiểm tra, cài Python (nếu cần) và thiết lập các thư viện.

---

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
