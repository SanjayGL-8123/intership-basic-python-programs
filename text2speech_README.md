# Offline Text-to-Speech Engine (`text2speech.py`)

Synthesizes spoken natural speech from text using the cross-platform, offline `pyttsx3` library.

---

## 📋 Overview

Unlike cloud-based speech APIs that require an internet connection and API keys, `pyttsx3` hooks directly into the host operating system's native speech synthesis engine (SAPI5 on Windows, NSSpeechSynthesizer on macOS, eSpeak on Linux).

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
python text2speech.py
```

---

## 🔍 Code Breakdown

```python
import pyttsx3

# Initialize the speech engine instance
engine = pyttsx3.init()

# Queue speech text
engine.say('Hello sanjay, how may I help you, sanjay. good Morning')

# Process queued commands and wait for speech to finish
engine.runAndWait()
```

### Key Concepts:
- `pyttsx3.init()`: Creates a factory instance of the speech synthesizer engine.
- `engine.say(text)`: Queues the text string into the speech synthesis queue.
- `engine.runAndWait()`: Blocks execution while processing all queued speech commands, allowing audio playback to complete before the program exits.
