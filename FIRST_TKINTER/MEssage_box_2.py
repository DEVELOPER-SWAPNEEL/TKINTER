from tkinter import *
window=Tk()
window.title("ALTIER")
window.geometry("500x600")
#THIS IS ONE WAY OF GENERATING THE MESSAGE
'''message=Message(window,text="WELCOME USER!",relief="raised",padx=50,pady=50)
message.pack()'''
#IN THE FOLLOWING WAY WE ARE TAKING THE MESSAGE IN THE CODE WITH A VARIABLE MY_VAR THEN PASSING IT IN MY_MESSAGE
#THEN WE SET THE MESSAGE IN THE MY_VAR.SET AND WRITE THE MESSAGE
#---------------------------------------------------------------------------------------------------------------
'''my_var=StringVar()
my_message=Message(window,textvariable=my_var,relief="raised",padx=50,pady=50)
my_var.set("WELCOME DUDE!!")
my_message.pack()'''
#---------------------------------------------------------------------------------------------------------------
show_msg=StringVar()
ent_var=StringVar()
my_message=Message(window,textvariable=show_msg,relief=RAISED,padx=50,pady=50)
def work():
    result=my_entry.get()
    show_msg.set(result)
my_entry=Entry(window,textvariable=ent_var,width=50,relief=RAISED)
btn=Button(window,text="OK",bg="black",fg="red",cursor="hand1",command=work)
my_message.pack()
my_entry.pack()
btn.pack()
window.mainloop()