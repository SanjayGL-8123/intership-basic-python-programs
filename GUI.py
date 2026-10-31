import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *
from PIL import ImageTk, Image
import numpy as np

np.set_printoptions(suppress=True)

top = tk.Tk()
top.geometry('800x600')
top.title('Project GUI Detection')

from pathlib import Path
sea_path = Path(__file__).resolve().parent / 'sea.jpg'
img = ImageTk.PhotoImage(Image.open(sea_path), master=top)
img_label = Label(top, image=img)
img_label.place(x=0, y=0)


def show_classify_button():
    classify_b = Button(
        top,
        text="Classify Image",
        padx=10,
        pady=5
    )

    classify_b.configure(
        background='#364156',
        foreground='white',
        font=('arial', 10, 'bold')
    )

    classify_b.place(relx=0.79, rely=0.46)



def upload_image():
    try:
        file_path = filedialog.askopenfilename()

        if not file_path:
            return

        uploaded = Image.open(file_path)

        uploaded.thumbnail(
            (
                top.winfo_width() / 1.25,
                top.winfo_height() / 1.25
            )
        )

        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im

        show_classify_button()

    except Exception as e:
        messagebox.showerror(
            "Error",
            "Unable to open image.\n" + str(e)
        )



sign_image = Label(top)
sign_image.place(relx=0.35, rely=0.20)



upload = Button(
    top,
    text="Upload an image",
    padx=10,
    pady=5,
    command=upload_image,
    font=('arial', 10, 'bold')
)

upload.configure(
    background='red',
    foreground='white'
)

upload.place(relx=0.45, rely=0.70)



heading = Label(
    top,
    text="Project GUI",
    pady=20,
    font=('arial', 20, 'bold')
)

heading.configure(
    background='black',
    foreground='white'
)

heading.pack()



top.mainloop()