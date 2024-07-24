from tkinter import *
from tkinter import font as tkfont

# Create the main window
window = Tk()
window.title("Royal Calculator")
window.geometry("400x500")
window.configure(bg='#1e1e2f')

# Define fonts and colors
entry_font = tkfont.Font(family='Helvetica', size=18, weight='bold')
button_font = tkfont.Font(family='Helvetica', size=14, weight='bold')
bg_color = '#2d2d44'
button_color = '#4b4b6b'
button_text_color = '#ffffff'
entry_bg = '#ffffff'
entry_fg = '#000000'

# Create the entry box
entry = Entry(window, font=entry_font, bg=entry_bg, fg=entry_fg, bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Define button click event
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, END)

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def button_operation(operator):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + operator)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create buttons using a loop
for (text, row, col) in buttons:
    if text == 'C':
        Button(window, text=text, font=button_font, bg='#ff6666', fg=button_text_color, 
padx=20, pady=20, command=button_clear).grid(row=row, column=col, columnspan=4, sticky="nsew")
    elif text == '=':
        Button(window, text=text, font=button_font, bg='#66ff66', fg=button_text_color, 
padx=20, pady=20, command=button_equal).grid(row=row, column=col, sticky="nsew")
    elif text in '0123456789':
        Button(window, text=text, font=button_font, bg=button_color, fg=button_text_color, 
padx=20, pady=20, command=lambda text=text: button_click(text)).grid(row=row, column=col, sticky="nsew")
    else:
        Button(window, text=text, font=button_font, bg=button_color, fg=button_text_color, 
padx=20, pady=20, command=lambda text=text: button_operation(text)).grid(row=row, column=col, sticky="nsew")

# Configure row and column weights for resizing
for i in range(1, 6):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Start the Tkinter main loop
window.mainloop()
