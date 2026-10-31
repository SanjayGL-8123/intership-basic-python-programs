import cv2
import tkinter as tk
from tkinter import messagebox
# from PIL import Image, ImageTk


def capture_image():
    cap = cv2.VideoCapture(0)  # Open webcam
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured_image.jpg", frame)
        messagebox.showinfo("Success", "Image Captured Successfully!")
        # cv2.imshow("captured_image.jpg")
    else:
        messagebox.showerror("Error", "Failed to Capture Image")
    cap.release()


# Create GUI window
root = tk.Tk()
root.title("Image Capture")
root.geometry("400x400")

capture_btn = tk.Button(root, text="Capture Image", command=capture_image)
capture_btn.pack()

root.mainloop()