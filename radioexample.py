import tkinter as tk


def show_selection():
    selected = var.get()
    label_result.config(text=f"You selected: {selected}")


root = tk.Tk()
root.title("Radio Button Example")
root.geometry("300x200")

var = tk.StringVar(value="male")

radio1 = tk.Radiobutton(root, text="male", variable=var, value="male")
radio2 = tk.Radiobutton(root, text="Female", variable=var, value="female")
radio3 = tk.Radiobutton(root, text="others", variable=var, value="others")

# Place radio buttons
radio1.pack(anchor="w")
radio2.pack(anchor="w")
radio3.pack(anchor="w")

btn_show = tk.Button(root, text="Show Selection", command=show_selection)
btn_show.pack(pady=10)

label_result = tk.Label(root, text="You selected: ")
label_result.pack()

root.mainloop()
