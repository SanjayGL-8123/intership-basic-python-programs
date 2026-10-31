from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Create an instance of tkinter frame or window
win = Tk()

# Set the geometry of tkinter frame
win.geometry("750x250")

def get_value():
    e_text = entry.get()
    messagebox.showinfo('You Typed', e_text)

# Create an Entry Widget

label1 = ttk.Label(win, text="Textbox example", font=('Century 35 bold'))
label1.pack(pady=30)

entry = ttk.Entry(win, font=('Century 12 bold'), width=40)
entry.pack(pady=30)

# Create a button to display the text of entry widget
button = ttk.Button(win, text="Sumbit", command=get_value)
button.pack()

win.mainloop()