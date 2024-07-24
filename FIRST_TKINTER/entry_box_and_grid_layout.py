from tkinter import *
window= Tk()
window.title("ALTIER")
window.geometry("500x600")
label_1=Label(window,text="MAIL")
lable_2=Label(window,text="Password")
entry_1=Entry(window,border=5,width=40)
entry_2=Entry(window,border=5,width=40)
label_1.grid(row=0,column=1)
lable_2.grid(row=1,column=1)
entry_1.grid(row=0,column=2)
entry_2.grid(row=1,column=2)

window.mainloop()