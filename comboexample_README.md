# Dropdown Combobox Example (`comboexample.py`)

A desktop GUI demonstrating the dropdown selection menu using Tkinter's `ttk.Combobox` widget.

---

## 📋 Overview

Dropdown lists (comboboxes) conserve screen space while giving users an easy-to-use list of predefined options. This app allows selecting a month from January through December and displays the choice on screen.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** `tkinter` (built-in standard library)

---

## 🚀 How to Run

```powershell
python comboexample.py
```

---

## 🔍 Code Breakdown

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Month Selector")
root.geometry("300x150")

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

month_cb = ttk.Combobox(root, values=months, state="readonly")
month_cb.set("Select a month")
month_cb.pack(pady=30)

selected_label = tk.Label(root, text="selected month", font=("Arial", 12))
selected_label.pack()

def show_selected_month():
    selected = month_cb.get()
    if selected == "Select a month":
        selected_label.config(text="Please choose a month.")
    else:
        selected_label.config(text=f"You selected: {selected}")

show_button = tk.Button(root, text="Show Month", command=show_selected_month)
show_button.pack(pady=10)

root.mainloop()
```

### Key Concepts:
- `ttk.Combobox(..., values=months, state="readonly")`: Creates the dropdown with month names. Setting `state="readonly"` prevents the user from typing arbitrary text.
- `month_cb.set(...)`: Sets placeholder text when the window opens.
- `month_cb.get()`: Reads the currently selected string.
