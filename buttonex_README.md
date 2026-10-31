# Basic Button Example (`buttonex.py`)

Demonstrates how to create and position a Tkinter `Button` widget using relative coordinate placement (`place`).

---

## 📋 Overview

Buttons are one of the most common user interface controls. This script introduces the `Button` widget and shows how to position it using proportional/relative placement within a 550x600 window.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** `tkinter` (built-in standard library)

---

## 🚀 How to Run

```powershell
python buttonex.py
```

---

## 🔍 Code Breakdown

```python
from tkinter import *

top = Tk()
top.geometry("550x600")
top.title("First button")

b = Button(top, text="My button")
b.place(relx=0.50, rely=0.60)
top.mainloop()
```

### Key Concepts:
- `Button(top, text="My button")`: Creates a button widget child of window `top` with the label `"My button"`.
- `b.place(relx=0.50, rely=0.60)`:
  - `relx=0.50`: Centers horizontally at 50% of parent width.
  - `rely=0.60`: Positions vertically at 60% of parent height.
  - Relative positioning (`relx`, `rely`) scales smoothly as the window is resized.
