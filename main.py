from tkinter import *
window = Tk()

window.geometry("600x400")
window.title("Midterm in OOP")

name=Label(window,text="Enter your Full name:",fg="red")
name.place(x=80,y=120)
namebox=Entry(window,bd=5,font=("veradana",15))
namebox.place(x=270,y=120)

def Myname():
    fullname = Label(window, text=namebox.get(), bd=3, bg="white", font = ("verdana", 12))
    fullname.place(x=274, y=195)

click=Button(window,text="Click to display your full name",fg="red",command=Myname)
click.place(x=80,y=190)
box=Entry(window,bd=5,font=("veradana",15))
box.place(x=270,y=190)


window.mainloop()