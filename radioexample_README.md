# Radio Button Selection Example (`radioexample.py`)

A graphical interface showing how to implement mutually exclusive single-choice options using Tkinter `Radiobutton` widgets.

---

## 📋 Overview

Radio buttons let users pick exactly one option from a predefined group. This example creates options for Gender selection (Male, Female, Others) bound to a shared `tk.StringVar`.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** `tkinter` (built-in standard library)

---

## 🚀 How to Run

```powershell
python radioexample.py
```

---

## 🔍 Code Breakdown

```python
import tkinter as tk

def show_selection():
    selected = var.get()
    label_result.config(text=f"You selected: {selected}")

root = tk.Tk()
root.title("Radio Button Example")
root.geometry("300x200")

var = tk.StringVar(value="male")

radio1 = tk.Radiobutton(root, text="male", variable=var, value="male")
radio2 = tk.Radiobutton(root, text="Female", variable=var, value="female")
radio3 = tk.Radiobutton(root, text="others", variable=var, value="others")

radio1.pack(anchor="w")
radio2.pack(anchor="w")
radio3.pack(anchor="w")

btn_show = tk.Button(root, text="Show Selection", command=show_selection)
btn_show.pack(pady=10)

label_result = tk.Label(root, text="You selected: ")
label_result.pack()

root.mainloop()
```

### Key Concepts:
- `var = tk.StringVar(value="male")`: A Tkinter string variable that tracks which radio button is active. Setting an initial value automatically selects that option on startup.
- `variable=var, value="value_name"`: By pointing multiple `Radiobutton` widgets to the same `variable`, Tkinter groups them together so selecting one unselects all others.
- `label_result.config(...)`: Dynamically updates the text property of an existing label without recreating it.
