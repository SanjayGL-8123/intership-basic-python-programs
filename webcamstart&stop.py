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
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)

            video_label.after(10, show_frame)


def stop_webcam():
    global running, cap

    running = False

    if cap is not None:
        cap.release()
        cap = None

    video_label.configure(image='')


# Create GUI window
root = tk.Tk()
root.title("Webcam Controller")
root.geometry("800x600")


# Video frame
frame = tk.Frame(root)
frame.pack(side=tk.LEFT, padx=20, pady=20)

video_label = tk.Label(frame)
video_label.pack()


# Control frame
control_frame = tk.Frame(root)
control_frame.pack(side=tk.RIGHT, padx=20, pady=20)


# Start button
start_btn = tk.Button(
    control_frame,
    text="Start Webcam",
    command=start_webcam
)
start_btn.pack()


# Stop button
stop_btn = tk.Button(
    control_frame,
    text="Stop Webcam",
    command=stop_webcam
)
stop_btn.pack()


root.mainloop()