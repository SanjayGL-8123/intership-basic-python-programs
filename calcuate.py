import tkinter as tk
from functools import partial


def call_result(label_result, n1, n2):
    num1 = float(n1.get())
    num2 = float(n2.get())

    result = num1 + num2
    label_result.config(text="Result = %g" % result)


def call_result2(label_result, n1, n2):
    num1 = float(n1.get())
    num2 = float(n2.get())

    result = num1 - num2
    label_result.config(text="Result = %g" % result)


def call_result3(label_result, n1, n2):
    num1 = float(n1.get())
    num2 = float(n2.get())

    result = num1 * num2
    label_result.config(text="Result = %g" % result)


def call_result4(label_result, n1, n2):
    num1 = float(n1.get())
    num2 = float(n2.get())

    if num2 == 0:
        label_result.config(text="Cannot divide by zero")
    else:
        result = num1 / num2
        label_result.config(text="Result = %g" % result)


root = tk.Tk()
root.geometry('400x300')
root.title('Calculator')

number1 = tk.StringVar()
number2 = tk.StringVar()

tk.Label(root, text="Enter first number").grid(row=1, column=0)
tk.Label(root, text="Enter second number").grid(row=2, column=0)

labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)

tk.Entry(root, textvariable=number1).grid(row=1, column=2)
tk.Entry(root, textvariable=number2).grid(row=2, column=2)

tk.Button(
    root,
    text="Add",
    command=partial(call_result, labelResult, number1, number2)
).grid(row=3, column=0)

tk.Button(
    root,
    text="Subtract",
    command=partial(call_result2, labelResult, number1, number2)
).grid(row=3, column=1)

tk.Button(
    root,
    text="Multiply",
    command=partial(call_result3, labelResult, number1, number2)
).grid(row=3, column=2)

tk.Button(
    root,
    text="Divide",
    command=partial(call_result4, labelResult, number1, number2)
).grid(row=3, column=3)

root.mainloop()