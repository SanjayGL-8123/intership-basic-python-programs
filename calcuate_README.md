# Four-Operation GUI Calculator (`calcuate.py`)

A graphical desktop calculator built with Tkinter featuring addition, subtraction, multiplication, and division with error handling for division by zero.

---

## 📋 Overview

Provides two number input boxes and four operation buttons arranged cleanly in a grid. It uses `functools.partial` to bind parameters to button callbacks dynamically and outputs the formatted calculation result.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** `tkinter` (built-in standard library)

---

## 🚀 How to Run

```powershell
python calcuate.py
```

---

## 🔍 Code Breakdown

```python
import tkinter as tk
from functools import partial

def call_result(label_result, n1, n2):
    num1 = float(n1.get())
    num2 = float(n2.get())
    result = num1 + num2
    label_result.config(text="Result = %g" % result)

def call_result2(label_result, n1, n2):
    num1 = float(n1.get())
    num2 = float(n2.get())
    result = num1 - num2
    label_result.config(text="Result = %g" % result)

def call_result3(label_result, n1, n2):
    num1 = float(n1.get())
    num2 = float(n2.get())
    result = num1 * num2
    label_result.config(text="Result = %g" % result)

def call_result4(label_result, n1, n2):
    num1 = float(n1.get())
    num2 = float(n2.get())
    if num2 == 0:
        label_result.config(text="Cannot divide by zero")
    else:
        result = num1 / num2
        label_result.config(text="Result = %g" % result)
```

### Key Concepts:
- **`functools.partial`**: Passes arguments (target result label and input StringVar instances) to callback functions directly inside button commands.
- **Float conversion (`float(...)`)**: Supports both whole integers and decimal inputs.
- **Format Specifier `%g`**: Automatically formats numbers cleanly (omitting unnecessary trailing decimal zeros, e.g. `5` instead of `5.0`).
- **Zero-Division Check**: Safeguards against crashing when dividing by zero.
- **Grid Layout (`.grid(row=..., column=...)`)**: Organizes labels, text entry fields, and action buttons in a table format.
