from tkinter import *

window=Tk()
window.title("shyam")
window.configure(background="black")
#Label
Label(text="mnsnzANSK",font="bold").grid(row=0,column=0)

#photo
pic=PhotoImage(file="C:\\Users\\DELL\\Downloads\\weather\\cloudy.png")
Label(image=pic,width=10,height=10).grid(row=1,column=1)
#textfield
Entry(bg="white").grid(row=2,column=2)
#botton
Button(text="submit").grid(row=3,column=3)
window.mainloop()