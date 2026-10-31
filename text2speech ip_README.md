# Interactive Text-to-Speech Converter (`text2speech ip.py`)

An interactive console program that takes any custom text typed by the user and vocalizes it through the system speakers using `pyttsx3`.

---

## 📋 Overview

Takes user input from the console and immediately speaks the text out loud through an offline text-to-speech engine.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.9 (Installed: Python 3.9.4)
- **Required Libraries:**
  ```powershell
  pip install pyttsx3
  ```
  *(Status: **Installed** ✅ `pyttsx3==2.99`, `pywin32==312`, `comtypes==1.4.17` in Python 3.9).*

---

## 🚀 How to Run

```powershell
python "text2speech ip.py"
```

> **Note:** Filename contains spaces, so enclose it in quotes when running.

---

## 🔍 Code Breakdown

```python
import pyttsx3

engine = pyttsx3.init()

text = input("enter some text: ")

engine.say(text)
engine.runAndWait()
```

### Key Concepts:
- `input(...)`: Accepts dynamic string input typed by the user.
- `engine.say(text)`: Converts the runtime variable `text` to phonemes and audio waveforms.
- `engine.runAndWait()`: Plays the generated voice audio and blocks until playback finishes.

---

## 💡 Example Run

```text
enter some text: Welcome to Python programming!
[Audio plays: "Welcome to Python programming!"]
```
