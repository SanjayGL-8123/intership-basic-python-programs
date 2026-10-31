import tkinter as tk
from tkinter import messagebox

from PIL.ImageTk import PhotoImage
# pip install pillow


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login Success", "Welcome!")
    else:
        messagebox.showerror(
            "Login Failed",
            "Invalid username or password"
        )



root = tk.Tk()
root.title("Login Page")
root.geometry("500x200")


from pathlib import Path
from PIL import Image
sea_path = Path(__file__).resolve().parent / "sea.jpg"
img = PhotoImage(Image.open(sea_path), master=root)
img_label = tk.Label(root, image=img)
img_label.place(x=0, y=0)

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()


tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()


login_btn = tk.Button(
    root,
    text="Login",
    command=login
)
login_btn.pack()


root.mainloop()