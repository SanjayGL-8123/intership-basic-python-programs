# Voting Eligibility Checker (`ifexample.py`)

A simple Python program that determines whether an individual is eligible to vote based on legal age.

---

## 📋 Overview

In most countries, the legal age for voting is 18 years. This script asks for the user's age and checks if they are 18 or older using a standard `if-else` statement.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** None (standard library only)

---

## 🚀 How to Run

```powershell
python ifexample.py
```

---

## 🔍 Code Breakdown

```python
age = int(input("enter age"))
print(age)
if age < 18:
    print("you are not eligible to vote")
else:
    print("you are eligible to vote")
```

### Key Concepts:
- `int(...)`: Parses user input string into an integer value for mathematical comparison.
- `if age < 18`: Evaluates if the entered number is strictly less than 18.
- `else`: Executed when `age >= 18`.

---

## 💡 Example Runs

### Example 1: Eligible
```text
enter age: 19
19
you are eligible to vote
```

### Example 2: Ineligible
```text
enter age: 15
15
you are not eligible to vote
```
