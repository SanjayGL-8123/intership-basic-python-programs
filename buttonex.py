# python application to create a simple button

from tkinter import *

top = Tk()
top.geometry("550x600")
top.title("First button")

b = Button(top, text="My button")
# b.pack()
b.place(relx=0.50, rely=0.60)
top.mainloop()