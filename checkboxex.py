import tkinter as tk


def show_selected_courses():

    selected = [course for course, var in course_vars.items() if var.get()]


    if selected:
        result_label.config(text=f"Selected Courses:\n{', '.join(selected)}")
    else:
        result_label.config(text="No courses selected.")


root = tk.Tk()
root.title("Course Selection")
root.geometry("400x350")


courses = ["Python Programming", "Data Science", "Web Development", "Machine Learning", "Cyber Security"]


course_vars = {}


title_label = tk.Label(root, text="Select the courses you want to enroll in:", font=("Arial", 12, "bold"))
title_label.pack(pady=15)
for course in courses:

    var = tk.BooleanVar(value=False)
    course_vars[course] = var


    cb = tk.Checkbutton(root, text=course, variable=var, font=("Arial", 10))
    cb.pack(anchor="w", padx=50, pady=5)

submit_btn = tk.Button(root, text="Submit Selection", command=show_selected_courses, bg="#4CAF50", fg="white",
                       font=("Arial", 10, "bold"))
submit_btn.pack(pady=20)


result_label = tk.Label(root, text="", font=("Arial", 11, "italic"), fg="#333333")
result_label.pack(pady=10)


root.mainloop()