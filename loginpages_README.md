# Graphical Login Interface with Background Image (`loginpages.py`)

A graphical user authentication interface created with Tkinter and Pillow (PIL), featuring a background image, masked password field, and alert popups.

---

## 📋 Overview

Provides a login window with:
- Background image loaded via Pillow (`sea.jpg`).
- Username entry field.
- Password entry field with character masking (`*`).
- Credential validation checking for `admin` / `password`.
- Informative message dialogs for successful and failed logins.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x (Tested on Python 3.9.4)
- **Required Libraries:**
  ```powershell
  pip install pillow
  ```
  *(Status: **Installed** ✅ `pillow==11.3.0`)*
- **Required Assets:** `sea.jpg` must be present in the same directory as the script.

---

## 🚀 How to Run

```powershell
python loginpages.py
```

---

## 🔍 Code Breakdown

```python
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from PIL import Image
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
root.geometry("500x200")

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

login_btn = tk.Button(root, text="Login", command=login)
login_btn.pack()

root.mainloop()
```

### Key Concepts:
- `Path(__file__).resolve().parent / "sea.jpg"`: Safely constructs an absolute path to the image asset relative to the script file.
- `PhotoImage(Image.open(...), master=root)`: Loads and adapts the image for Tkinter rendering.
- `Entry(..., show="*")`: Replaces input characters with asterisks for password confidentiality.
- Default credentials:
  - **Username:** `admin`
  - **Password:** `password`
