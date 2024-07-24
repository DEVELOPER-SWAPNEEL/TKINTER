from tkinter import *
window=Tk()
window.title("ALTIER")
window.geometry("500x600")
def login_entry():
    print("LOGIN SUCCESSFUL!!")
button_1=Button(window,text="LOGIN",background="red",fg="black",command=login_entry,activebackground="black"
                ,activeforeground="red",cursor="hand1",width=12,font=("bold",12))
button_1.pack()
window.mainloop()