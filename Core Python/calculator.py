import tkinter as tk

# Create window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

# Display
display = tk.Entry(window, font=("Arial", 20), justify="right")
display.pack(fill="x", padx=10, pady=10)


# Functions
def click(number):
    display.insert(tk.END, number)


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Create frame for buttons
button_frame = tk.Frame(window)
button_frame.pack()


# Buttons
buttons = [
    ("7", 0, 0),
    ("8", 0, 1),
    ("9", 0, 2),
    ("/", 0, 3),

    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("*", 1, 3),

    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("-", 2, 3),

    ("0", 3, 0),
    (".", 3, 1),
    ("+", 3, 2),
    ("=", 3, 3)
]


for text, row, column in buttons:

    if text == "=":
        button = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 15),
            command=calculate
        )
    else:
        button = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 15),
            command=lambda x=text: click(x)
        )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5,
        ipadx=15,
        ipady=10
    )


# Clear button
clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 15),
    command=clear
)

clear_button.grid(
    row=4,
    column=0,
    columnspan=4,
    padx=5,
    pady=10,
    ipadx=30,
    ipady=10
)


# Run calculator
window.mainloop()