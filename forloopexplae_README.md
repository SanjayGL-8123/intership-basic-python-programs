# For and While Loop Examples (`forloopexplae.py`)

A tutorial script demonstrating list traversal with `for` loops, range-based indexing, and conditional filtering with `while` loops.

---

## 📋 Overview

This script explores three loop patterns in Python:
1. Iterating through a Python list using indices (`for i in range(len(...))`).
2. A `while` loop filtering and printing numbers divisible by 5 or 7 within the range 1 to 30.
3. A sequential `while` loop counting numbers from 1 to 30.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** None (standard library only)

---

## 🚀 How to Run

```powershell
python forloopexplae.py
```

---

## 🔍 Code Breakdown

```python
mylist = [4.2, 5, 7, 2, 4, 84]

for i in range(len(mylist)):
    print(mylist[i], end=" ")

print("\n")

i = 1
while i <= 30:
    if i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")
    i += 1

print("\n")

k = 1
while k <= 30:
    print(k, end=" ")
    k += 1
```

### Key Concepts:
- `len(mylist)`: Returns the total number of items in the list.
- `end=" "`: Specifies a space delimiter instead of a default newline character for consecutive prints on the same line.
- `i % 5 == 0 or i % 7 == 0`: Modulo operator `%` computes remainder. This condition checks divisibility by 5 or 7.
- `i += 1`: Loop increment statement preventing infinite execution.

---

## 💡 Output

```text
4.2 5 7 2 4 84 

5 7 10 14 15 20 21 25 28 30 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 
```
