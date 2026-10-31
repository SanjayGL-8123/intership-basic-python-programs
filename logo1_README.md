# Centered Themed Login Screen (`logo1.py`)

A graphical login window with custom background artwork (`bg4.png`) and centered widget positioning using relative and absolute coordinates.

---

## 📋 Overview

Demonstrates precise control over GUI positioning using `place(relx=..., y=..., anchor="center")`. Labels and text entry fields are cleanly aligned down the vertical center of the window over a background banner.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x (Tested on Python 3.9.4)
- **Required Libraries:**
  ```powershell
  pip install pillow
  ```
  *(Status: **Installed** ✅ `pillow==11.3.0`)*
- **Required Assets:** `bg4.png` must be present in the workspace root.

---

## 🚀 How to Run

```powershell
python logo1.py
```

---

## 🔍 Code Breakdown

```python
import tkinter as tk
from tkinter import messagebox
from PIL.ImageTk import PhotoImage

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login Success", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = tk.Tk()
root.title("Login Page")
root.geometry("500x300")

# Background image
img = PhotoImage(file="bg4.png", master=root)
img_label = tk.Label(root, image=img)
img_label.place(x=0, y=0)

# Form widgets with centered coordinates
tk.Label(root, text="Username:", bg="white").place(relx=0.5, y=80, anchor="center")
username_entry = tk.Entry(root, width=25)
username_entry.place(relx=0.5, y=110, anchor="center")

tk.Label(root, text="Password:", bg="white").place(relx=0.5, y=145, anchor="center")
password_entry = tk.Entry(root, width=25, show="*")
password_entry.place(relx=0.5, y=175, anchor="center")

login_btn = tk.Button(root, text="Login", width=10, command=login)
login_btn.place(relx=0.5, y=220, anchor="center")

root.mainloop()
```

### Key Concepts:
- `place(relx=0.5, y=..., anchor="center")`: Horizontally centers widgets regardless of window width variations.
- `bg="white"`: Creates a contrasting background behind label texts over the background graphic.
- Valid login credentials:
  - **Username:** `admin`
  - **Password:** `password`
