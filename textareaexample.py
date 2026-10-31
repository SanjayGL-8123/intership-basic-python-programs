import tkinter as tk

root = tk.Tk()

l = tk.Label(root, text="Fact Viewer")
T = tk.Text(root, height=5, width=40)

Fact = "This is the first fact."

def nextfunction():
    nexttext = """Hi, good morning.
This is my next text."""
    T.delete("1.0", tk.END)
    T.insert(tk.END, nexttext)

b1 = tk.Button(root, text="Next", command=nextfunction)
b2 = tk.Button(root, text="Exit", command=root.destroy)

l.pack()
T.pack()
b1.pack()
b2.pack()

T.insert(tk.END, Fact)

root.mainloop()