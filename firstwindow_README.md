# Minimal Tkinter Window (`firstwindow.py`)

A starter template illustrating the essential structure of a Tkinter Desktop GUI application.

---

## 📋 Overview

Every Tkinter GUI application requires at least three steps:
1. Creating the root/main window (`Tk()`).
2. Setting window configurations (dimensions and title).
3. Starting the event listening loop (`mainloop()`).

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** `tkinter` (comes bundled with standard Python on Windows and macOS).

---

## 🚀 How to Run

```powershell
python firstwindow.py
```

---

## 🔍 Code Breakdown

```python
from tkinter import *

top = Tk()
top.geometry('600x400')
top.title("my First window")
top.mainloop()
```

### Key Concepts:
- `top = Tk()`: Instantiates the master application window.
- `top.geometry('600x400')`: Sets the initial window size to 600 pixels wide by 400 pixels high.
- `top.title("my First window")`: Sets the title in the window's title bar.
- `top.mainloop()`: Runs the GUI event loop, waiting for user interactions (clicks, keyboard input, closing the window).
