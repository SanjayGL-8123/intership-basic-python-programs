# Multiplication Table Generator (`forloop_table.py`)

A basic command-line tool that calculates and displays the multiplication table (from 1 to 10) for any chosen number.

---

## 📋 Overview

Takes a single number from the user and iterates through numbers 1 to 10 using a `for` loop, printing the product for each step.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** None (standard library only)

---

## 🚀 How to Run

```powershell
python forloop_table.py
```

---

## 🔍 Code Breakdown

```python
num = int(input("enter a number"))
res = 0
for i in range(1, 11):
    res = num * i
    print(res)
```

### Key Concepts:
- `int(input(...))`: Reads console input and parses it into an integer.
- `range(1, 11)`: Generates multipliers 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
- `num * i`: Computes the arithmetic product of the base number and current multiplier.

---

## 💡 Example Run

```text
enter a number: 7
7
14
21
28
35
42
49
56
63
70
```
