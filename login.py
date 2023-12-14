import tkinter as tk
from ttkbootstrap import Style
from PIL import ImageTk, Image
import time
import os

# Önceden belirlenmiş şifreler listesi
passwords = ["18811938", "your_old_password", "another_old_password"]
current_password_index = 0

last_password_change = time.time()  # Şu anki zamanı al
change_interval = 30 * 24 * 60 * 60  # 30 gün = 30 * 24 saat * 60 dakika * 60 saniye

def check_credentials():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Kullanıcı adı ve şifre kontrolü
    if entered_username == "emusoft.ai" and entered_password == "18811938":
        root.destroy()
        os.system("python main.py")

    else:
        access_granted_label.config(text="Giriş başarısız! Lütfen tekrar deneyin.", fg="red")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

def open_contact_window():
    contact_window = tk.Toplevel(root)
    contact_window.title("İletişim Bilgileri")

    developer_info = """
    Geliştiriciler:
    - Kaan Acar
    - Mehmet Oktar Önder
    - Elifnaz Çelik

    İletişim:
    Email: kaanacar@skiff.com
    Email: oktar.onder@gmail.com
    Email: d.elifcelik@gmail.com
    """

    developer_info_label = tk.Label(contact_window, text=developer_info, font=('Garamond', 14, "bold"))
    developer_info_label.pack()
    contact_window.iconbitmap("logo.ico")
    contact_window.minsize(300, 300)

def check_password_change():
    global current_password_index, last_password_change

    current_time = time.time()
    time_remaining = change_interval - (current_time - last_password_change)

    # Eğer son şifre değişikliği üzerinden belirli bir süre geçtiyse, şifreyi değiştir
    if current_time - last_password_change >= change_interval:
        if current_password_index < len(passwords) - 1:
            current_password_index += 1
        else:
            current_password_index = 0

        last_password_change = current_time  # Yeni zamanı güncelle

        access_granted_label.config(text="Şifre değiştirildi. Yeni şifre kullanılabilir.", fg="green")
    else:
        # Şifre değiştirme zamanı değilse, kullanıcıya bilgi ver ve geri sayımı göster
        access_granted_label.config(text=f"Şifre zaten güncel. Değişikliğe kalan süre: {int(time_remaining/60)} dakika", fg="black")

    # 1 dakika sonra tekrar kontrol et
    root.after(60000, check_password_change)  # 60 saniye * 1000 milisaniye = 60000 milisaniye


def center_window(window, width, height):
    # Ekranın genişliği ve yüksekliği
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Pencereyi ortalamak için hesaplamalar
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window_width = 450
window_height = 500
# Ana pencere oluşturma
root = tk.Tk()
root.overrideredirect(1)
window_width = 450
window_height = 500
root.title("emusoft.ai/Yazılım ve Yapay Zeka Geliştirme Kulübü")
root.iconbitmap("logo.ico")

# Pencerenin boyutunu sabitler


# Stili Tkinter için ayarla
style = Style(theme='flatly')


# Devam eden kod
# Geliştirici bilgisi resmi
developer_info_img = Image.open("emusoft.ai.png")
developer_info_img = developer_info_img.resize((200, 200), Image.LANCZOS)
developer_info_img = ImageTk.PhotoImage(developer_info_img)

# Geliştirici bilgisi paneli
developer_info_panel = tk.Label(root, image=developer_info_img)
developer_info_panel.pack()

# Geliştirici yazısı
developer_text = tk.Label(root, text="Sendificate", font=('Brush Script MT', 50, "bold"), fg="dark blue")
developer_text.pack()

# Kullanıcı adı girişi
username_label = tk.Label(root, text="Kullanıcı Adı:", font=("Now", 10, "bold"))
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

# Şifre girişi
password_label = tk.Label(root, text="Şifre:", font=("Now", 10, "bold"))
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Giriş butonu
submit_button = tk.Button(root, text="Giriş Yap", command=check_credentials)
submit_button.pack()

# Bilgilendirme etiketi
access_granted_label = tk.Label(root, text="", fg="black")
access_granted_label.pack()

# Ek metin ve İletişim butonu
additional_text = tk.Label(root, text="Soru ve iş birlikleriniz için; ", font=('Garamond', 14, "bold"))
additional_text.pack()

contact_button = tk.Button(root, text="İletişim", command=open_contact_window, font=('Garamond', 12, "bold"))
contact_button.pack()

additional_text = tk.Label(root, text="", font=('Garamond', 14, "bold"))
additional_text.pack()

check_password_change()
center_window(root, window_width, window_height)
root.mainloop()

