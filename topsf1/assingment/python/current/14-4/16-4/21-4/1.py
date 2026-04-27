import tkinter
from tkinter import ttk,messagebox

tk=tkinter.Tk()
tk.title("my-apps")
tk.config(background="red")
tk.geometry("400x400")

def add():
    n1=int(t1.get())
    n2=int(t2.get())
    print("plus",int(n1)+int(n2))
def minus():
    n1=int(t1.get())
    n2=int(t2.get())
    print("plus",int(n1)-int(n2))
    
def mul():
    n1=int(t1.get())
    n2=int(t2.get())
    print("plus",int(n1)*int(n2))
def div():
    n1=int(t1.get())
    n2=int(t2.get())
    print("plus",int(n1)/int(n2))

t1=tkinter.Entry()
t1.grid(row=0,column=1,sticky='w')
t1.place(x=10,y=20)

t2=tkinter.Entry()
t2.grid(row=0,column=2,sticky='w')
t2.place(x=10,y=60)

t3=tkinter.Entry()
t3.grid(row=0,column=2,sticky='w')
t3.place(x=10,y=210)

btn1=tkinter.Button(text="+",fg='red',font='Elephant 15 bold',command=add)
btn1.place(x=50,y=150)
btn2=tkinter.Button(text="-",fg='red',font='Elephant 15 bold',command=minus)
btn2.place(x=100,y=150)
btn3=tkinter.Button(text="*",fg='red',font='Elephant 15 bold',command=mul)
btn3.place(x=150,y=150)
btn4=tkinter.Button(text="/",fg='red',font='Elephant 15 bold',command=div)
btn4.place(x=200,y=150)










tk.mainloop()
