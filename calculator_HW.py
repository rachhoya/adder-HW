from tkinter import *

window=Tk()
window.geometry("450x300")
window.title("Mini Adder")
window.config(background="pink")

def add_number():
    number=int(box1.get())
    number2=int(box2.get())
    total=number+number2
    result=Label(window,text="Result:" + str(total),font=("Arial",15,"bold"))
    result.place(x=170,y=200)


box1=Entry(window,width=30)
box1.place(x=130,y=90)

box2=Entry(window,width=30)
box2.place(x=130,y=50)

add=Button(window,text="Add",bg="white",font=("Arial",15,"bold"),bd=3,relief="raised",command=add_number)
add.place(x=190,y=130)

window.mainloop()