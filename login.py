import tkinter as tk
from ttkbootstrap import Style
from PIL import ImageTk, Image
import os


def exit_application():
    root.destroy()
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


# Stili Tkinter için ayarla
style = Style(theme='flatly')

# Geliştirici bilgisi resmi
developer_info_img = Image.open("emusoft.ai.png")
developer_info_img = developer_info_img.resize((200, 200), Image.LANCZOS)
developer_info_img = ImageTk.PhotoImage(developer_info_img)

# Geliştirici bilgisi paneli
developer_info_panel = tk.Label(root, image=developer_info_img)
developer_info_panel.pack()

# Geliştirici yazısı
developer_text = tk.Label(root, text="Sendificate", font=('Brush Script MT', 50, "bold"), fg='dark blue')
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

# Ek Yazı
additional_text = tk.Label(root, text="", font=('Garamond', 5, "bold"))
additional_text.pack()

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

exit_button = tk.Button(root, text="X", command=exit_application, bg='red', fg='white', font=('Arial', 10, 'bold'))
exit_button.place(relx=1, x=-2, y=2, anchor='ne')

center_window(root, window_width, window_height)
root.mainloop()

