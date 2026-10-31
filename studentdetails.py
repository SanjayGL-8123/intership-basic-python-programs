import tkinter as tk
from tkinter import messagebox


def submit_data():
    name = name_entry.get()
    gender = gender_var.get()
    email = email_entry.get()
    address = address_entry.get("1.0", tk.END).strip()
    city = city_entry.get()

    # Format the collected data
    student_info = (
        f"Name: {name}\n"
        f"Gender: {gender}\n"
        f"Email: {email}\n"
        "--------------------\n"
        f"Address: {address}\n"
        f"City: {city}"
    )

    # Show data in message box
    messagebox.showinfo("Student Information", student_info)


# Tkinter window setup
root = tk.Tk()
root.title("Student Data Form")
root.geometry("400x500")


# Name
tk.Label(root, text="Name:").pack(anchor="w", padx=10, pady=5)

name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=10)


# Gender
tk.Label(root, text="Gender:").pack(anchor="w", padx=10, pady=5)

gender_var = tk.StringVar(value="Male")

tk.Radiobutton(
    root,
    text="Male",
    variable=gender_var,
    value="Male"
).pack(anchor="w", padx=20)

tk.Radiobutton(
    root,
    text="Female",
    variable=gender_var,
    value="Female"
).pack(anchor="w", padx=20)

tk.Radiobutton(
    root,
    text="Other",
    variable=gender_var,
    value="Other"
).pack(anchor="w", padx=20)


# Email
tk.Label(root, text="Email:").pack(anchor="w", padx=10, pady=5)

email_entry = tk.Entry(root, width=40)
email_entry.pack(padx=10)


# Address
tk.Label(root, text="Address:").pack(anchor="w", padx=10, pady=5)

address_entry = tk.Text(root, width=30, height=4)
address_entry.pack(padx=10)


# City
tk.Label(root, text="City:").pack(anchor="w", padx=10, pady=5)

city_entry = tk.Entry(root, width=40)
city_entry.pack(padx=10)


# Submit Button
submit_button = tk.Button(
    root,
    text="Submit",
    command=submit_data
)
submit_button.pack(pady=20)


# Run the application
root.mainloop()
