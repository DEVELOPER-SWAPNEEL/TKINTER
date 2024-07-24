from tkinter import *
window=Tk()
window.title("ALTIER")
lable_1=Label(window,text="LABLE_1",bg="purple",fg="white")
lable_2=Label(window,text="LABLE_2",bg="blue",fg="white")
lable_3=Label(window,text="LABLE_3",bg="gold",fg="black")
lable_1.pack(side=TOP,fill=X,expand=False)
lable_2.pack(side=LEFT,fill=Y,expand=False)
lable_3.pack(side=RIGHT,fill=Y,expand=False)
#HERE WITHIN THE FILL OPTION WE HAVE PROVIDED WITH A METHOD FILL WHICH REFERS TO THE VERTIVAL(Y-AXIS)OR 
#HORIZONTAL (X-AXIS)
#IN PACK WE CAN USE ONLY 3 TYPES OF METHODS SIDE(TOP,BOTTOM,LEFT AND RIGHT),FILL (ORIENTATION),
#EXPAND IS A TOOL WHICH RECIEVES ACTIONS BASED ON BOOLIAN TYPE SO IF EXPAND IS TRUE THEN IT LEAVES SPACE FOR MARGIN
window.geometry("500x600")
window.mainloop()
