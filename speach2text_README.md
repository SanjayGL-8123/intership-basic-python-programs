# Microphone Speech-to-Text Recognition (`speach2text.py`)

Captures spoken audio from the system microphone and transcribes it into text using Google's Speech Recognition API.

---

## 📋 Overview

Uses Python's `speech_recognition` module to record voice from an active microphone input, automatically adjust for room background noise, send the audio packet to Google's speech recognition engine, and output the transcribed string.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.9 (Installed: Python 3.9.4)
- **Required Libraries:**
  ```powershell
  pip install SpeechRecognition PyAudio
  ```
  *(Status: **Installed** ✅ `SpeechRecognition==3.17.0`, `PyAudio==0.2.14` in Python 3.9).*
  *(Important: Note the package name is `SpeechRecognition` without underscores, not `speech_recognition`).*
- **Hardware & Network:** Active microphone and internet access (for Google Speech API communication).

---

## 🚀 How to Run

```powershell
python speach2text.py
```

---

## 🔍 Code Breakdown

```python
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")

    # Calibrate energy threshold based on ambient environmental noise
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

    try:
        # Transcribe audio using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said:", text)

    except sr.UnknownValueError:
        print("Could not understand the audio")

    except sr.RequestError:
        print("Could not request results, check your internet connection")
```

### Key Concepts:
- `sr.Microphone()`: Context manager opening the default audio recording device.
- `recognizer.adjust_for_ambient_noise(source)`: Samples ambient room silence to filter background hum.
- `recognizer.listen(source)`: Records until the user stops speaking.
- `recognizer.recognize_google(...)`: Sends audio data to Google's free speech-to-text endpoint.
- Robust Exception Handling:
  - `UnknownValueError`: Handles unintelligible speech or silence.
  - `RequestError`: Handles API connection dropouts or offline network status.
