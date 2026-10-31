# Student Registration Form (`studentdetails.py`)

A comprehensive data entry form GUI built in Tkinter that captures student details and displays them formatted in a popup dialog.

---

## 📋 Overview

Demonstrates combining multiple input widget types into a coherent registration form:
- **Name:** Single-line text `Entry`
- **Gender:** Radiobuttons (`Male`, `Female`, `Other`)
- **Email:** Single-line text `Entry`
- **Address:** Multi-line `Text` widget
- **City:** Single-line text `Entry`
- **Submit:** Form validation and summary message box display

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** `tkinter` (built-in standard library)

---

## 🚀 How to Run

```powershell
python studentdetails.py
```

---

## 🔍 Code Breakdown

```python
import tkinter as tk
from tkinter import messagebox

def submit_data():
    name = name_entry.get()
    gender = gender_var.get()
    email = email_entry.get()
    address = address_entry.get("1.0", tk.END).strip()
    city = city_entry.get()

    student_info = (
        f"Name: {name}\n"
        f"Gender: {gender}\n"
        f"Email: {email}\n"
        "--------------------\n"
        f"Address: {address}\n"
        f"City: {city}"
    )

    messagebox.showinfo("Student Information", student_info)
```

### Key Concepts:
- `address_entry.get("1.0", tk.END).strip()`: Reads all lines from the `tk.Text` widget and removes trailing newlines.
- `gender_var.get()`: Retrieves the string value from whichever radio button is selected.
- F-string formatting compiles the fields into a multi-line formatted profile.
- Grouping inputs with labels and consistent padding (`padx`, `pady`, `anchor="w"`).
