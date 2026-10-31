# Textbox & Entry Input Example (`textboxex.py`)

A themed Tkinter application using `ttk.Entry` and `ttk.Button` to capture user input and display it in a popup alert.

---

## 📋 Overview

Shows how to accept text input from a user using ttk widgets, read the entered text on button press, and display it inside a `messagebox` dialog.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** `tkinter` (built-in standard library)

---

## 🚀 How to Run

```powershell
python textboxex.py
```

---

## 🔍 Code Breakdown

```python
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win = Tk()
win.geometry("750x250")

def get_value():
    e_text = entry.get()
    messagebox.showinfo('You Typed', e_text)

label1 = ttk.Label(win, text="Textbox example", font=('Century 35 bold'))
label1.pack(pady=30)

entry = ttk.Entry(win, font=('Century 12 bold'), width=40)
entry.pack(pady=30)

button = ttk.Button(win, text="Submit", command=get_value)
button.pack()

win.mainloop()
```

### Key Concepts:
- `ttk.Entry`: Modern styled single-line text input field.
- `entry.get()`: Retrieves the current string entered into the input box.
- `messagebox.showinfo(title, message)`: Opens a native system message dialog with an OK button.
- `command=get_value`: Binds the button click event to the Python function `get_value`.
