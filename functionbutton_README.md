# Colored Action Buttons & Layouts (`functionbutton.py`)

A colorful Tkinter application demonstrating side-based layout positioning (`pack(side=...)`), button styling, and separate callback alerts for multiple buttons.

---

## 📋 Overview

This application places four uniquely styled buttons along each border of the window (Left, Right, Top, Bottom). Clicking any button triggers an associated information alert dialog using `messagebox.showinfo`.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** `tkinter` (built-in standard library)

---

## 🚀 How to Run

```powershell
python functionbutton.py
```

---

## 🔍 Code Breakdown

```python
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("400x400")

def redfun():
    messagebox.showinfo("Hello", "Red Button clicked")

def bluefun():
    messagebox.showinfo("Hello", "blue Button clicked")

def greenfun():
    messagebox.showinfo("Hello", "green Button clicked")

def yellowfun():
    messagebox.showinfo("Hello", "yellow Button clicked")

b1 = Button(top, text="Red", command=redfun, activeforeground="red", activebackground="gold", pady=10, padx=10)
b2 = Button(top, text="Blue", command=bluefun, activeforeground="blue", activebackground="orange", pady=10, padx=10)
b3 = Button(top, text="Green", command=greenfun, activeforeground="white", activebackground="green", pady=10, padx=10)
b4 = Button(top, text="Yellow", command=yellowfun, activeforeground="yellow", activebackground="brown", pady=10, padx=10)

b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=TOP)
b4.pack(side=BOTTOM)

top.mainloop()
```

### Key Concepts:
- `side=LEFT / RIGHT / TOP / BOTTOM`: Aligns widgets along designated container edges.
- `activeforeground` / `activebackground`: Colors applied when the user clicks and holds the button down.
- `padx` / `pady`: Adds internal padding inside button borders.
- Dedicated handler functions (`redfun`, `bluefun`, etc.) invoked via `command=...`.
