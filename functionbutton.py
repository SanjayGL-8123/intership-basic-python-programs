from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("400x400")

def redfun():
    messagebox.showinfo("Hello", "Red Button clicked")

def bluefun():
    messagebox.showinfo("Hello", "blue Button clicked")

def greenfun():
    messagebox.showinfo("Hello", "green Button clicked")

def yellowfun():
    messagebox.showinfo("Hello", "yellow Button clicked")

b1 = Button(top, text="Red", command=redfun, activeforeground="red", activebackground="gold", pady=10, padx=10)

b2 = Button(top, text="Blue", command=bluefun, activeforeground="blue", activebackground="orange", pady=10, padx=10)

b3 = Button(top, text="Green", command=greenfun, activeforeground="white", activebackground="green", pady=10, padx=10)

# Fixed: Changed "brown5" to a valid color like "brown" or a hex code
b4 = Button(top, text="Yellow", command=yellowfun, activeforeground="yellow", activebackground="brown", pady=10, padx=10)

b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=TOP)
b4.pack(side=BOTTOM)

top.mainloop()