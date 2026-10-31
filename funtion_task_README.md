# Basic Arithmetic Functions (`funtion_task.py`)

A modular script defining separate mathematical functions for addition, subtraction, multiplication, and division.

---

## 📋 Overview

Demonstrates how to break arithmetic operations into individual, single-responsibility functions:
- `addnum(n1, n2)`: Computes and prints sum
- `subnum(n1, n2)`: Computes and prints difference
- `mulnum(n1, n2)`: Computes and prints product
- `divnum(n1, n2)`: Computes and prints quotient

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** None (standard library only)

---

## 🚀 How to Run

```powershell
python funtion_task.py
```

---

## 🔍 Code Breakdown

```python
def addnum(n1, n2):
    sum = n1 + n2
    print(sum)

def subnum(n1, n2):
    sub = n1 - n2
    print(sub)

def mulnum(n1, n2):
    pro = n1 * n2
    print(pro)

def divnum(n1, n2):
    div = n1 / n2
    print(div)

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))

addnum(num1, num2)
subnum(num1, num2)
mulnum(num1, num2)
divnum(num1, num2)
```

### Key Concepts:
- **Modular Code:** Each math operation is encapsulated in its own function.
- **Multiple Function Calls:** The same inputs `(num1, num2)` are passed sequentially to each function.
- Division operator `/` in Python 3 returns a floating-point number.

---

## 💡 Example Run

```text
enter first number: 20
enter second number: 5
25
15
100
4.0
```
