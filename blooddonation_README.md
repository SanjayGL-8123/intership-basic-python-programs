# Blood Donation Eligibility Checker (`blooddonation.py`)

A simple Python console application that checks whether a user meets the minimum age and weight requirements to donate blood.

---

## 📋 Overview

Donating blood requires meeting specific health criteria:
1. **Age Requirement:** Must be at least 18 years old.
2. **Weight Requirement:** Must be at least 50 kg.

This program uses nested conditional statements (`if-else`) to evaluate user inputs and provide immediate feedback on eligibility.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** None (standard library only)

---

## 🚀 How to Run

Execute the script from your terminal or command prompt:

```powershell
python blooddonation.py
```

---

## 🔍 Code Breakdown

```python
age = int(input("enter age:"))
weight = int(input("enter weight"))

if age >= 18:
    if weight >= 50:
        print("you are eligible to donate blood")
    else:
        print("you are not eligible to donate blood, you are under weight")
else:
    print("you are not eligible to donate blood, you are under age")
```

### Key Concepts:
- `input()`: Captures user input as a string.
- `int(...)`: Converts input string into an integer.
- **Nested `if-else`**:
  - The outer `if age >= 18` checks age first. If younger than 18, it fails immediately with an underweight check bypassed.
  - The inner `if weight >= 50` validates weight only if age meets the criteria.

---

## 💡 Example Runs

### Example 1: Eligible Donor
```text
enter age: 22
enter weight: 65
you are eligible to donate blood
```

### Example 2: Underweight
```text
enter age: 20
enter weight: 45
you are not eligible to donate blood, you are under weight
```

### Example 3: Underage
```text
enter age: 16
enter weight: 55
you are not eligible to donate blood, you are under age
```
