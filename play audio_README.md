# Audio Music Playback Script (`play audio.py`)

A clean example of background music playback in Python using Pygame's mixer module with explanatory lifecycle comments.

---

## 📋 Overview

Demonstrates how to play digital audio files asynchronously while keeping the script alive using an execution wait loop. Without this loop, the script would exit immediately after initiating playback, cutting off sound before it starts.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x (Tested on Python 3.9.4)
- **Required Libraries:**
  ```powershell
  pip install pygame
  ```
  *(Status: **Installed** ✅ `pygame==2.6.1`)*
- **Required Audio File:** `Thalapathy Vetri Kondan.mp3` in the workspace directory.

---

## 🚀 How to Run

```powershell
python "play audio.py"
```

> **Tip:** Always enclose filenames containing spaces within quotation marks in PowerShell or Command Prompt.

---

## 🔍 Code Breakdown

```python
import pygame
import time

pygame.mixer.init()

pygame.mixer.music.load("Thalapathy Vetri Kondan.mp3")

pygame.mixer.music.play()

# Keep script running while music plays
# Otherwise, the script ends and the sound stops immediately
while pygame.mixer.music.get_busy():
    time.sleep(1)
```

### Key Concepts:
- **Asynchronous Audio Streaming:** `play()` initiates playback in a separate audio thread.
- **Process Lifecycle Synchronization:** The `while pygame.mixer.music.get_busy()` loop polls the audio channel state every second until playback concludes.
