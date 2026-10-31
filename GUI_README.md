# Image Upload and Classifier GUI (`GUI.py`)

A graphical interface application designed for image loading, preview thumbnail scaling, and initiating image classification workflows.

---

## 📋 Overview

Acts as a frontend prototype for machine learning / computer vision image classification models:
- Displays a themed window with a background backdrop (`sea.jpg`).
- Allows the user to select an image from their local machine using `filedialog.askopenfilename()`.
- Generates a proportional thumbnail scaled to the window dimensions.
- Displays the loaded image preview.
- Reveals a "Classify Image" action button once an image is uploaded.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x (Tested on Python 3.9.4)
- **Required Libraries:**
  ```powershell
  pip install pillow numpy
  ```
  *(Status: **Installed** ✅ `pillow==11.3.0`, `numpy==2.0.2`)*
- **Required Assets:** `sea.jpg` in the script directory.

---

## 🚀 How to Run

```powershell
python GUI.py
```

---

## 🔍 Code Breakdown

```python
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
from pathlib import Path

# Load background
sea_path = Path(__file__).resolve().parent / 'sea.jpg'
img = ImageTk.PhotoImage(Image.open(sea_path), master=top)
img_label = Label(top, image=img)
img_label.place(x=0, y=0)

def show_classify_button():
    classify_b = Button(top, text="Classify Image", padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        uploaded = Image.open(file_path)
        uploaded.thumbnail((top.winfo_width() / 1.25, top.winfo_height() / 1.25))

        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im

        show_classify_button()
    except Exception as e:
        messagebox.showerror("Error", "Unable to open image.\n" + str(e))
```

### Key Concepts:
- `filedialog.askopenfilename()`: Opens the native OS file picker dialog to let users choose an image file (e.g. `.jpg`, `.png`).
- `uploaded.thumbnail(...)`: Scales the image proportionally without distortion to fit comfortably inside the application frame.
- Garbage Collection Prevention: Assigning `sign_image.image = im` retains a reference in Python, preventing Tkinter from dropping the image due to garbage collection.
- Progressive Disclosure: The classification trigger button is hidden until the user successfully uploads an image.
