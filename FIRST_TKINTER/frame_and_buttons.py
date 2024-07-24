from tkinter import *
window=Tk()
window.title("ALTIER")
window.geometry("500x600")
window.config(bg="black")
#NOW WE WILL ADD FRAMES TO THE WINDOW 
frame_1=Frame(window,width=300,height=200,cursor="hand1")
frame_1.pack(side=TOP)
frame_2=Frame(window,width=300,height=200,cursor="cross")
frame_2.pack(side=BOTTOM)
#NOW WITHIN THE FRAME WE CAN PUT BUTTONS
Button_1=Button(frame_1,text="PRESS HERE",bg="red")
Button_2=Button(frame_2,text="MR. BEEN",bg="GREEN")
Button_3=Button(frame_1,text="NEW TRY",fg="blue")
Button_1.pack()
Button_2.pack()
Button_3.pack()
window.mainloop()