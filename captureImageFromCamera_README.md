# Camera Snapshot Capture Tool (`captureImageFromCamera.py`)

A desktop GUI tool combining Tkinter and OpenCV to capture a single photo from a webcam and save it to disk.

---

## 📋 Overview

Clicking the **Capture Image** button opens the local webcam, captures a live video frame, writes the frame to `captured_image.jpg`, releases the camera hardware, and displays a confirmation dialog.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x (Tested on Python 3.9.4)
- **Required Libraries:**
  ```powershell
  pip install opencv-python
  ```
  *(Status: **Installed** ✅ `opencv-python==5.0.0.93`, Tkinter is included in standard Python).*
- **Hardware:** Connected webcam / camera device.

---

## 🚀 How to Run

```powershell
python captureImageFromCamera.py
```

---

## 🔍 Code Breakdown

```python
import cv2
import tkinter as tk
from tkinter import messagebox

def capture_image():
    cap = cv2.VideoCapture(0)  # Open default camera index 0
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured_image.jpg", frame)
        messagebox.showinfo("Success", "Image Captured Successfully!")
    else:
        messagebox.showerror("Error", "Failed to Capture Image")
    cap.release()

root = tk.Tk()
root.title("Image Capture")
root.geometry("400x400")

capture_btn = tk.Button(root, text="Capture Image", command=capture_image)
capture_btn.pack()

root.mainloop()
```

### Key Concepts:
- `cv2.VideoCapture(0)`: Accesses the default hardware video input (camera index 0).
- `ret, frame = cap.read()`:
  - `ret`: Boolean status flag indicating successful frame acquisition.
  - `frame`: NumPy image array representing the captured camera frame.
- `cv2.imwrite("captured_image.jpg", frame)`: Encodes and saves the image file to disk.
- `cap.release()`: Critical cleanup function releasing the camera driver so other applications can access it.
- **Output:** Creates `captured_image.jpg` in the current working directory.
