# Loop Control Statements Example (`breakex.py`)

A beginner-friendly demonstration of Python's loop control keywords: `break` and `continue`.

---

## 📋 Overview

Loop control statements change the execution from its normal sequence:
- **`break` statement:** Terminates the loop immediately when a condition is met, jumping out of the loop body.
- **`continue` statement:** Skips the rest of the current iteration and jumps directly to the next cycle of the loop.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** None (standard library only)

---

## 🚀 How to Run

```powershell
python breakex.py
```

---

## 🔍 Code Breakdown

```python
print("Break ...")
for num in range(1, 11):
    if num == 6:
        break
    print(num)

print("Continue ...")
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)
```

### Key Concepts:
1. `range(1, 11)`: Generates numbers starting from 1 up to 10 (upper bound 11 is exclusive).
2. **`break` in action:** When `num` reaches 6, the loop terminates. Numbers 6 through 10 are never processed.
3. **`continue` in action:** When `num % 2 == 0` (even numbers), `continue` skips the `print(num)` statement, printing only odd numbers.

---

## 💡 Output

```text
Break ...
1
2
3
4
5
Continue ...
1
3
5
7
9
```
