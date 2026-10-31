# Multi-Selection Checkbox Example (`checkboxex.py`)

A course enrollment interface demonstrating multiple-choice selection using Tkinter `Checkbutton` widgets and dynamic dictionary state tracking.

---

## 📋 Overview

Unlike radio buttons, checkbuttons allow multiple simultaneous selections. This application loops through a list of available tech courses, creates a checkbox for each one, and displays a summary of all selected courses upon clicking "Submit Selection".

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** `tkinter` (built-in standard library)

---

## 🚀 How to Run

```powershell
python checkboxex.py
```

---

## 🔍 Code Breakdown

```python
import tkinter as tk

def show_selected_courses():
    selected = [course for course, var in course_vars.items() if var.get()]
    if selected:
        result_label.config(text=f"Selected Courses:\n{', '.join(selected)}")
    else:
        result_label.config(text="No courses selected.")

root = tk.Tk()
root.title("Course Selection")
root.geometry("400x350")

courses = ["Python Programming", "Data Science", "Web Development", "Machine Learning", "Cyber Security"]
course_vars = {}

title_label = tk.Label(root, text="Select the courses you want to enroll in:", font=("Arial", 12, "bold"))
title_label.pack(pady=15)

for course in courses:
    var = tk.BooleanVar(value=False)
    course_vars[course] = var
    cb = tk.Checkbutton(root, text=course, variable=var, font=("Arial", 10))
    cb.pack(anchor="w", padx=50, pady=5)

submit_btn = tk.Button(root, text="Submit Selection", command=show_selected_courses, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
submit_btn.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 11, "italic"), fg="#333333")
result_label.pack(pady=10)

root.mainloop()
```

### Key Concepts:
- `course_vars = {}`: A dictionary mapping each course name to its corresponding `BooleanVar`.
- `var = tk.BooleanVar(value=False)`: Stores the boolean checked (`True`) or unchecked (`False`) state.
- List comprehension `[c for c, v in course_vars.items() if v.get()]`: Extracts names of all checked courses concisely.
- `", ".join(selected)`: Formats the selected items into a readable comma-separated list.
