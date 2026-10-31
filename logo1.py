import tkinter as tk
from tkinter import messagebox
from PIL.ImageTk import PhotoImage


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


# Create GUI window
root = tk.Tk()
root.title("Login Page")
root.geometry("500x300")

# Background image
img = PhotoImage(file="bg4.png", master=root)

img_label = tk.Label(root, image=img)
img_label.place(x=0, y=0)


tk.Label(root, text="Username:", bg="white").place(
    relx=0.5, y=80, anchor="center"
)


username_entry = tk.Entry(root, width=25)
username_entry.place(
    relx=0.5, y=110, anchor="center"
)



tk.Label(root, text="Password:", bg="white").place(
    relx=0.5, y=145, anchor="center"
)


password_entry = tk.Entry(root, width=25, show="*")
password_entry.place(
    relx=0.5, y=175, anchor="center"
)



login_btn = tk.Button(
    root,
    text="Login",
    width=10,
    command=login
)

login_btn.place(
    relx=0.5, y=220, anchor="center"
)


root.mainloop()