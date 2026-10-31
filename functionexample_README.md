# User Authentication with Functions (`functionexample.py`)

A simple console-based authentication script demonstrating parameterized functions and credential validation.

---

## 📋 Overview

This script defines an authentication function that accepts username and password parameters, verifies them against hardcoded credentials (`admin` / `password`), and prints whether the login succeeded or failed.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x
- **External Libraries:** None (standard library only)

---

## 🚀 How to Run

```powershell
python functionexample.py
```

---

## 🔍 Code Breakdown

```python
def check(un, pw):
    print("this is my function")
    if un == "admin" and pw == "password":
        print("login success")
    else:
        print("login failed")

s1 = input("enter user name \n")
s2 = input("enter password \n")

check(s1, s2)
```

### Key Concepts:
- **Function Parameters:** `un` and `pw` act as placeholders for the arguments passed when invoking `check(...)`.
- **Logical AND (`and`):** Both conditions (`un == "admin"` and `pw == "password"`) must evaluate to `True` for authentication to succeed.
- **Passing Arguments:** `check(s1, s2)` passes user inputs `s1` and `s2` into the function.

---

## 💡 Example Runs

### Successful Login:
```text
enter user name 
admin
enter password 
password
this is my function
login success
```

### Failed Login:
```text
enter user name 
admin
enter password 
1234
this is my function
login failed
```
