import tkinter as tk
def update_display(value):
    current_text = display_label.cget("text")
    new_text = current_text + value
    display_label.config(text=new_text)


def clear_display():
    display_label.config(text="")


def calculate():
    try:
        expression = display_label.cget("text")
        result = eval(expression)
        display_label.config(text=str(result))
    except:
        display_label.config(text="Error")


root = tk.Tk()
root.title("Button Calculator")


display_label = tk.Label(root, text="", relief=tk.RIDGE, font=("Helvetica", 24), anchor=tk.E)
display_label.grid(row=0, column=0, columnspan=4, sticky=tk.N+tk.S+tk.E+tk.W)


buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3),
]

for text, row, column in buttons:
    button = tk.Button(root, text=text, font=("Helvetica", 15), command=lambda t=text: update_display(t))
    button.grid(row=row, column=column, sticky=tk.N+tk.S+tk.E+tk.W)


clear_button = tk.Button(root, text="clear", font=("Helvetica", 15), command=clear_display)
clear_button.grid(row=5, column=0, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)


calculate_button = tk.Button(root, text="=", font=("Helvetica", 15), command=calculate)
calculate_button.grid(row=5, column=2, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)


for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)


root.mainloop()