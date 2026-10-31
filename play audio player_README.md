# Background Audio Player (`play audio player.py`)

A Python audio playback script using the `pygame.mixer` module to load and play MP3 audio files.

---

## 📋 Overview

Initializes the Pygame audio mixer subsystem, loads the target audio file (`Thalapathy Vetri Kondan.mp3`), begins playback, and maintains a loop to keep the process alive until the song finishes.

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
python "play audio player.py"
```

> **Note:** Because the filename contains spaces, remember to wrap the filename in quotation marks when executing from the command line.

---

## 🔍 Code Breakdown

```python
import pygame
import time

# Initialize the mixer
pygame.mixer.init()

# Load audio file
pygame.mixer.music.load("Thalapathy Vetri Kondan.mp3")

# Begin playback
pygame.mixer.music.play()

# Keep script running while audio plays
while pygame.mixer.music.get_busy():
    time.sleep(1)
```

### Key Concepts:
- `pygame.mixer.init()`: Prepares the audio hardware and driver for sound synthesis and decoding.
- `pygame.mixer.music.load(...)`: Streams the MP3 track into the music playback channel without loading the entire uncompressed file into memory.
- `pygame.mixer.music.get_busy()`: Returns `True` as long as sound is actively playing, preventing the Python process from terminating prematurely.
- `time.sleep(1)`: Yields CPU execution for 1 second during each poll to avoid high CPU consumption.
