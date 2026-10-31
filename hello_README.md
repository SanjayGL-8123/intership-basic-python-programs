# Python Fundamentals & Data Types (`hello.py`)

A starter program exploring essential Python concepts including variables, data types, type checking, string slicing, and basic conditions.

---

## 📋 Overview

Covers foundational Python syntax:
- Variable declaration and automatic typing (`int`, `str`, `float`).
- Inspecting data types with `type()`.
- String slicing and reversing syntax (`[::-1]`).
- Print formatting and variable interpolation.
- Basic `if-else` comparison.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** None (standard library only)

---

## 🚀 How to Run

```powershell
python hello.py
```

---

## 🔍 Code Breakdown

```python
print("hello world")
x = 7
s1 = "Hello python"
y = 10.5

print(s1)
print(s1[::-1])
print(type(s1))
print(type(y))
print(type(x))

print("the value of x is:", x)
print("the string is :" + s1)
print("float value is :", y)

if x <= 10:
    print("x is less than 10")
else:
    print("x is greater than 10")
```

### Key Concepts:
- `s1[::-1]`: Extended slice syntax `[start:stop:step]` with a step of `-1` reverses the string.
- `type(var)`: Returns the class type of the variable (`<class 'str'>`, `<class 'int'>`, `<class 'float'>`).
- Multiple arguments in `print()`: Automatically inserts spaces between arguments.

---

## 💡 Output

```text
hello world
Hello python
nohtyp olleH
<class 'str'>
<class 'float'>
<class 'int'>
the value of x is: 7
the string is :Hello python
float value is : 10.5
x is less than 10
```
