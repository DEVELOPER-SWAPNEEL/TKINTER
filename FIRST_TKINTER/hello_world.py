# TKINTER IS A EXTENSION OF PYTHON USED TO MAKE GUI APPLICATIONS WHERE GUI IS
# GUI------->>GRAPHICAL USER INTERFACE


# STEP 1:- IMPORT TKINTER
from tkinter import *
# STEP 2:- GUI INTERACTION
window = Tk()
# here from the module tkinter we import a class called as Tk() assigned to object window
# STEP 3:- ADDING INPUTS
inp = Label(window, text="HELLO WORLD!!")
inp.pack()
# STEP 4:- MAIN LOOP
window.mainloop()
