from tkinter import *
import tkinter.messagebox
window=Tk()
tkinter.messagebox.showinfo("info","GOOD MORNING USER!")
tkinter.messagebox.showerror("ERROR","TIME OUT")
tkinter.messagebox.showwarning("FIRE","FIRE WARNING")
question=tkinter.messagebox.askyesno("weather","WILL IT RAIN?")
if  question == True:
    print("TAKE RAIN-COAT")
else:
    print("ARE YOU SURE IF THEN OK..")
window.mainloop()
