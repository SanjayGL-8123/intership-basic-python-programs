# Tkinter Embedded Webcam with Start & Stop Controls (`webcamstart&stop.py`)

Embeds a real-time OpenCV video stream directly inside a Tkinter desktop GUI with interactive start and stop controls.

---

## 📋 Overview

Rather than opening an external OpenCV window, this application embeds the camera stream inside a Tkinter `Label`. Users can click **Start Webcam** to open the camera stream and **Stop Webcam** to pause and release the camera device safely.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x (Tested on Python 3.9.4)
- **Required Libraries:**
  ```powershell
  pip install opencv-python pillow
  ```
  *(Status: **Installed** ✅ `opencv-python==5.0.0.93`, `pillow==11.3.0`)*
- **Hardware:** Connected webcam.

---

## 🚀 How to Run

```powershell
python "webcamstart&stop.py"
```

---

## 🔍 Code Breakdown

```python
import cv2
import tkinter as tk
from PIL import Image, ImageTk

cap = None
running = False

def start_webcam():
    global cap, running
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    running = True
    show_frame()

def show_frame():
    if running and cap is not None:
        ret, frame = cap.read()
        if ret:
            # OpenCV captures BGR; Tkinter/PIL requires RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)
            # Schedule the next frame in 10 ms (~60-100 fps max)
            video_label.after(10, show_frame)

def stop_webcam():
    global running, cap
    running = False
    if cap is not None:
        cap.release()
        cap = None
    video_label.configure(image='')
```

### Key Concepts:
- **Color Channel Conversion (`cv2.COLOR_BGR2RGB`):** OpenCV uses Blue-Green-Red channel ordering natively, whereas Pillow and Tkinter expect Red-Green-Blue.
- **Recursive Non-Blocking Frame Polling (`widget.after`):** Avoids blocking Tkinter's main event loop by scheduling `show_frame` execution every 10 milliseconds.
- **State Management:** Uses boolean flags and global camera handles to guarantee memory and hardware devices are released cleanly when paused or stopped.
