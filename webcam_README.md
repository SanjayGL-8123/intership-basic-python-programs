# Live OpenCV Webcam Feed (`webcam.py`)

A pure OpenCV script that streams video in real-time from a connected webcam with key-triggered exit.

---

## 📋 Overview

Captures continuous video frames from the webcam, displays them in a native OpenCV rendering window titled `Webcam`, and listens for the `a` keyboard press to cleanly close the video stream.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x (Tested on Python 3.9.4)
- **Required Libraries:**
  ```powershell
  pip install opencv-python
  ```
  *(Status: **Installed** ✅ `opencv-python==5.0.0.93`)*
- **Hardware:** Connected webcam.

---

## 🚀 How to Run

```powershell
python webcam.py
```

### Controls:
- Press the **`a`** key on your keyboard while focusing on the video window to stop and close the camera.

---

## 🔍 Code Breakdown

```python
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame. Check your network or URL.")
        break

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Key Concepts:
- `cv2.VideoCapture(0)`: Establishes a video stream connection to camera device 0.
- `cv2.imshow('Webcam', frame)`: Renders the image matrix in an OpenCV window.
- `cv2.waitKey(1) & 0xFF == ord('a')`:
  - `waitKey(1)` pauses execution for 1 millisecond to refresh the window event queue.
  - Bitwise masking `& 0xFF` ensures clean keycode comparison across different operating systems.
  - Matches ASCII code of character `'a'`.
- `cap.release()` & `cv2.destroyAllWindows()`: Closes hardware camera handles and destroys all active GUI windows.
