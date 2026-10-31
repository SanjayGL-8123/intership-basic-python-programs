import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Month Selector")
root.geometry("300x150")

# List of months
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
# Combobox for months
month_cb = ttk.Combobox(root, values=months, state="readonly")
month_cb.set("Select a month")
month_cb.pack(pady=30)


selected_label = tk.Label(root, text="selected month", font=("Arial", 12))
selected_label.pack()

def show_selected_month():
    selected = month_cb.get()

    if selected == "Select a month":
        selected_label.config(text="Please choose a month.")
    else:
        selected_label.config(text=f"You selected: {selected}")



show_button = tk.Button(root, text="Show Month", command=show_selected_month)
show_button.pack(pady=10)


root.mainloop()
