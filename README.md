# Basic Python Programs Repository

A structured collection of 33 beginner-to-intermediate Python scripts covering fundamental programming concepts, GUI development with Tkinter, computer vision with OpenCV, audio & speech processing, and data handling.

Each script has a dedicated companion `[filename]_README.md` documentation file located alongside it.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Python Environment & Installed Libraries](#-python-environment--installed-libraries)
- [Fixing the "No module named ..." Error (Python Interpreter Mismatch)](#-fixing-the-no-module-named--error-python-interpreter-mismatch)
- [Program Catalog by Category](#-program-catalog-by-category)
  - [1. Python Fundamentals & Control Flow](#1-python-fundamentals--control-flow)
  - [2. Functions & Modularity](#2-functions--modularity)
  - [3. Desktop GUI with Tkinter](#3-desktop-gui-with-tkinter)
  - [4. Audio Playback & Speech Processing (STT / TTS)](#4-audio-playback--speech-processing-stt--tts)
  - [5. Computer Vision & Webcam Streams](#5-computer-vision--webcam-streams)
  - [6. Data Handling & Utilities](#6-data-handling--utilities)
- [Asset Files & Resources](#-asset-files--resources)
- [Execution Guide](#-execution-guide)
- [Troubleshooting & FAQs](#-troubleshooting--faqs)

---

## 📦 Python Environment & Installed Libraries

All dependencies for all 33 programs are **100% installed and verified** in your Python 3.9 environment:
- **Python Executable:** `C:\Users\Sanjay G L\AppData\Local\Programs\Python\Python39\python.exe`
- **Python Version:** `Python 3.9.4`
- **Requirements File:** [`requirements.txt`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/requirements.txt)

### ✅ Complete Installed Libraries Roster

| Module / Library | Installed Version | Used In | Status |
| :--- | :--- | :--- | :--- |
| **`SpeechRecognition`** | `3.17.0` | [`speach2text.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/speach2text.py) (Microphone voice transcription) | **Installed** ✅ |
| **`PyAudio`** | `0.2.14` | [`speach2text.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/speach2text.py) (Microphone audio driver) | **Installed** ✅ |
| **`pyttsx3`** | `2.99` | [`text2speech.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/text2speech.py), [`text2speech ip.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/text2speech%20ip.py) (Offline TTS) | **Installed** ✅ |
| **`pywin32` / `comtypes`** | `312` / `1.4.17` | Windows SAPI5 audio backend for `pyttsx3` | **Installed** ✅ |
| **`opencv-python`** | `5.0.0.93` | [`webcam.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/webcam.py), [`captureImageFromCamera.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/captureImageFromCamera.py), [`webcamstart&stop.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/webcamstart&stop.py) | **Installed** ✅ |
| **`pillow`** | `11.3.0` | [`GUI.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/GUI.py), [`loginpages.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/loginpages.py), [`logo1.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/logo1.py), [`webcamstart&stop.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/webcamstart&stop.py), [`Qr code.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/Qr%20code.py) | **Installed** ✅ |
| **`pygame`** | `2.6.1` | [`play audio.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/play%20audio.py), [`play audio player.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/play%20audio%20player.py) | **Installed** ✅ |
| **`pandas`** | `2.3.3` | [`foodRecommandation.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/foodRecommandation.py) | **Installed** ✅ |
| **`qrcode`** | `8.2` | [`Qr code.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/Qr%20code.py) | **Installed** ✅ |
| **`numpy`** | `2.0.2` | Array processing & OpenCV frames | **Installed** ✅ |
| **`matplotlib`** | `3.9.4` | Data plotting & visualization | **Installed** ✅ |
| **`scikit-learn`** | `1.6.1` | Machine learning algorithms | **Installed** ✅ |
| **`scipy`** | `1.13.1` | Scientific computing | **Installed** ✅ |
| **`seaborn`** | `0.13.2` | Statistical data plotting | **Installed** ✅ |
| **`colorama`** | `0.4.6` | Terminal text formatting and colors | **Installed** ✅ |

---

## ⚠️ Fixing the "No module named ..." Error (Python Interpreter Mismatch)

If you see:
```text
Traceback (most recent call last):
  File "speach2text.py", line 1, in <module>
    import speech_recognition as sr
ModuleNotFoundError: No module named 'speech_recognition'
```
or `ModuleNotFoundError: No module named 'cv2'` / `'pyttsx3'` when clicking the **Run (Play)** button in your editor:

### 🔍 Why This Happens:
Your machine has **two separate Python environments**:
1. **Python 3.9 (System Python):** `C:\Users\Sanjay G L\AppData\Local\Programs\Python\Python39\python.exe`
   - **All libraries are installed here.** When you run `python filename.py` in the terminal, it works smoothly.
2. **`.venv` (UV / Python 3.14):** `c:\Users\Sanjay G L\Desktop\basic programs\.venv\Scripts\python.exe`
   - This `.venv` was created using Python 3.14 (an experimental alpha build) and does **not** have the libraries installed.
   - When you click the editor's "Play" button, your editor tries to run inside `.venv` instead of Python 3.9!

### 💡 Quick Solution (Switch Editor Interpreter to Python 3.9):
1. In your editor (VS Code / Antigravity), press:
   - **`Ctrl + Shift + P`**
2. Type and select:
   - **`Python: Select Interpreter`**
3. Select your installed **Python 3.9.4**:
   - `Python 3.9.4 ('Python39': C:\Users\Sanjay G L\AppData\Local\Programs\Python\Python39\python.exe)`
4. Now, whenever you click **Run (Play)**, your scripts will run using Python 3.9 where all packages are already installed and working!

### 💡 Alternatively, Run Directly from Terminal:
You can run any script directly using the standard `python` command:
```powershell
python speach2text.py
python "text2speech ip.py"
python webcam.py
```

> **Note on Package Names:** When installing speech recognition, the package name on PyPI is `SpeechRecognition` (without underscore), not `speech_recognition`:
> ```powershell
> pip install SpeechRecognition PyAudio
> ```

---

## 📚 Program Catalog by Category

### 1. Python Fundamentals & Control Flow

| Script | Documentation | Description | Dependencies | Status |
| :--- | :--- | :--- | :--- | :--- |
| [`hello.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/hello.py) | [`hello_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/hello_README.md) | Syntax basics, data types (`int`, `str`, `float`), slicing & reversing strings | Standard Library | Ready ✅ |
| [`gitinput.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/gitinput.py) | [`gitinput_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/gitinput_README.md) | Standard user input capture and string concatenation | Standard Library | Ready ✅ |
| [`ifexample.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/ifexample.py) | [`ifexample_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/ifexample_README.md) | Evaluates voting eligibility based on age threshold (18+) | Standard Library | Ready ✅ |
| [`blooddonation.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/blooddonation.py) | [`blooddonation_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/blooddonation_README.md) | Nested conditional logic validating age and weight requirements | Standard Library | Ready ✅ |
| [`breakex.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/breakex.py) | [`breakex_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/breakex_README.md) | Demonstrates loop disruption keywords (`break` and `continue`) | Standard Library | Ready ✅ |
| [`forloopexplae.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/forloopexplae.py) | [`forloopexplae_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/forloopexplae_README.md) | List traversal with `for` loops, range indexing, and modulo filtering in `while` loops | Standard Library | Ready ✅ |
| [`forloop_table.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/forloop_table.py) | [`forloop_table_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/forloop_table_README.md) | Computes and displays the multiplication table (1 to 10) for any input number | Standard Library | Ready ✅ |

---

### 2. Functions & Modularity

| Script | Documentation | Description | Dependencies | Status |
| :--- | :--- | :--- | :--- | :--- |
| [`function.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/function.py) | [`function_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/function_README.md) | Basic function declaration (`def`) and repeated invocation | Standard Library | Ready ✅ |
| [`functionexample.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/functionexample.py) | [`functionexample_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/functionexample_README.md) | Function with parameters (`un`, `pw`) for user credential verification | Standard Library | Ready ✅ |
| [`funtion_task.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/funtion_task.py) | [`funtion_task_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/funtion_task_README.md) | Modular math functions (`addnum`, `subnum`, `mulnum`, `divnum`) | Standard Library | Ready ✅ |

---

### 3. Desktop GUI with Tkinter

| Script | Documentation | Description | Primary Widgets | Status |
| :--- | :--- | :--- | :--- | :--- |
| [`firstwindow.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/firstwindow.py) | [`firstwindow_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/firstwindow_README.md) | Minimal Tkinter boilerplate template | `Tk`, `geometry`, `title`, `mainloop` | Ready ✅ |
| [`buttonex.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/buttonex.py) | [`buttonex_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/buttonex_README.md) | Basic button placement with relative positioning | `Button`, `place(relx, rely)` | Ready ✅ |
| [`textboxex.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/textboxex.py) | [`textboxex_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/textboxex_README.md) | Single-line text input field reading input on click | `ttk.Entry`, `ttk.Button`, `messagebox` | Ready ✅ |
| [`textareaexample.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/textareaexample.py) | [`textareaexample_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/textareaexample_README.md) | Multiline text display, dynamic text replacement, window exit | `tk.Text`, `insert`, `delete` | Ready ✅ |
| [`radioexample.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/radioexample.py) | [`radioexample_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/radioexample_README.md) | Mutually exclusive single-choice gender selection | `Radiobutton`, `StringVar` | Ready ✅ |
| [`checkboxex.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/checkboxex.py) | [`checkboxex_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/checkboxex_README.md) | Multiple-choice course enrollment selection form | `Checkbutton`, `BooleanVar` | Ready ✅ |
| [`comboexample.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/comboexample.py) | [`comboexample_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/comboexample.py) | Read-only dropdown list for selecting months | `ttk.Combobox`, `Label` | Ready ✅ |
| [`functionbutton.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/functionbutton.py) | [`functionbutton_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/functionbutton_README.md) | Border-aligned colored action buttons with alerts | `pack(side=LEFT/RIGHT/TOP/BOTTOM)` | Ready ✅ |
| [`calcuate.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/calcuate.py) | [`calcuate_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/calcuate_README.md) | 4-operation GUI calculator with zero-division handling | `grid()`, `functools.partial`, `StringVar` | Ready ✅ |
| [`studentdetails.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/studentdetails.py) | [`studentdetails_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/studentdetails_README.md) | Multi-field registration form (Name, Gender, Email, Address, City) | Form layout, `Entry`, `Radiobutton`, `Text` | Ready ✅ |
| [`loginpages.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/loginpages.py) | [`loginpages_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/loginpages_README.md) | Authentication window with background image backdrop (`sea.jpg`) | `pillow` (`11.3.0` installed) | Ready ✅ |
| [`logo1.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/logo1.py) | [`logo1_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/logo1_README.md) | Centered login screen with background banner (`bg4.png`) | `pillow` (`11.3.0` installed) | Ready ✅ |
| [`GUI.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/GUI.py) | [`GUI_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/GUI_README.md) | Image classification frontend with file browser & preview thumbnail | `pillow`, `numpy` (both installed) | Ready ✅ |

---

### 4. Audio Playback & Speech Processing (STT / TTS)

| Script | Documentation | Description | Required Libraries | Status |
| :--- | :--- | :--- | :--- | :--- |
| [`play audio player.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/play%20audio%20player.py) | [`play audio player_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/play%20audio%20player_README.md) | Plays MP3 audio tracks asynchronously | `pygame` (`2.6.1` installed) | Ready ✅ |
| [`play audio.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/play%20audio.py) | [`play audio_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/play%20audio_README.md) | Background audio player with process lifecycle explanation | `pygame` (`2.6.1` installed) | Ready ✅ |
| [`text2speech.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/text2speech.py) | [`text2speech_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/text2speech_README.md) | Offline voice synthesizer speaking predefined greetings | `pyttsx3` (`2.99` installed) | Ready ✅ |
| [`text2speech ip.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/text2speech%20ip.py) | [`text2speech ip_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/text2speech%20ip_README.md) | Interactive speech engine vocalizing custom user input | `pyttsx3` (`2.99` installed) | Ready ✅ |
| [`speach2text.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/speach2text.py) | [`speach2text_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/speach2text_README.md) | Records microphone audio and transcribes speech using Google Speech API | `SpeechRecognition` (`3.17.0`), `PyAudio` (`0.2.14`) | Ready ✅ |

---

### 5. Computer Vision & Webcam Streams

| Script | Documentation | Description | Libraries Used | Status |
| :--- | :--- | :--- | :--- | :--- |
| [`captureImageFromCamera.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/captureImageFromCamera.py) | [`captureImageFromCamera_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/captureImageFromCamera_README.md) | Tkinter GUI button that takes a webcam photo and saves `captured_image.jpg` | `opencv-python` (`5.0.0.93` installed) | Ready ✅ |
| [`webcam.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/webcam.py) | [`webcam_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/webcam_README.md) | Live OpenCV webcam stream with key 'a' to exit | `opencv-python` (`5.0.0.93` installed) | Ready ✅ |
| [`webcamstart&stop.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/webcamstart&stop.py) | [`webcamstart&stop_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/webcamstart&stop_README.md) | Embedded camera stream inside a Tkinter window with Start/Stop buttons | `opencv-python`, `pillow` (both installed) | Ready ✅ |

---

### 6. Data Handling & Utilities

| Script | Documentation | Description | Libraries & I/O | Status |
| :--- | :--- | :--- | :--- | :--- |
| [`foodRecommandation.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/foodRecommandation.py) | [`foodRecommandation_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/foodRecommandation_README.md) | Queries nutritional benefits & demerits for foods from CSV | `pandas` (`2.3.3` installed), `food_data.csv` | Ready ✅ |
| [`Qr code.py`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/Qr%20code.py) | [`Qr code_README.md`](file:///c:/Users/Sanjay%20G%20L/Desktop/basic%20programs/Qr%20code_README.md) | Generates custom-styled QR code image (white-on-red) from link | `qrcode` (`8.2`), `pillow` (both installed) | Ready ✅ |

---

## 📁 Asset Files & Resources

The repository includes accompanying data and media assets required by several scripts:
- `food_data.csv`: Tabular food benefits dataset used by `foodRecommandation.py`.
- `sea.jpg`: Background image used in `GUI.py` and `loginpages.py`.
- `bg4.png`: Background banner used in `logo1.py`.
- `Thalapathy Vetri Kondan.mp3`: Audio track played by `play audio.py` and `play audio player.py`.
- `captured_image.jpg`: Output generated by `captureImageFromCamera.py`.
- `qrcode.png`: Output generated by `Qr code.py`.
- `yolov8n.pt`: Pretrained YOLOv8 nano neural network weights file.

---

## ⚡ Execution Guide

Always execute scripts using Python 3. Remember to wrap filenames with spaces in quotation marks:

```powershell
# Standard scripts
python speach2text.py
python blooddonation.py
python calcuate.py
python studentdetails.py
python foodRecommandation.py

# Scripts with spaces in filenames
python "play audio player.py"
python "text2speech ip.py"
python "Qr code.py"
```

---

## 💡 Troubleshooting & FAQs

1. **`ModuleNotFoundError` when clicking the editor Run / Play button:**
   - Your editor is currently pointing to `.venv` (Python 3.14). Switch the Python interpreter to **Python 3.9** (`Ctrl + Shift + P` -> `Python: Select Interpreter` -> choose `Python 3.9.4`).
2. **`pip install speech_recognition` error:**
   - The official package name is case-insensitive but uses no underscores: `pip install SpeechRecognition PyAudio`.
3. **Camera fails to open in OpenCV / Tkinter:**
   - Ensure no other application (Zoom, Teams, Browser) is actively using the webcam.
   - If device index `0` fails, test index `1` if you have multiple cameras.
4. **Login credentials for GUI scripts:**
   - Default username: `admin`
   - Default password: `password`
