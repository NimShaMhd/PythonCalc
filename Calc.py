from tkinter import *
window=Tk()
window.geometry("300x300")
title=window.title("PyCalc")
content_widget = Label(text="Simple Calculator")
content_widget.pack()
button1=Button(text="1",height=1,width=1,bg="black",fg="yellow")
button1.pack()
button1.grid(row=0,column=2)
button2=Button(text="2",height=1,width=1,bg="black",fg="yellow")
button2.pack()
button3=Button(text="3",height=1,width=1,bg="black",fg="yellow")
button3.pack()
button4=Button(text="4",height=1,width=1,bg="black",fg="yellow")
button4.pack()
button5=Button(text="5",height=1,width=1,bg="black",fg="yellow")
button5.pack()
button6=Button(text="6",height=1,width=1,bg="black",fg="yellow")
button6.pack()
button7=Button(text="7",height=1,width=1,bg="black",fg="yellow")
button7.pack()
button8=Button(text="8",height=1,width=1,bg="black",fg="yellow")
button8.pack()
button9=Button(text="9",height=1,width=1,bg="black",fg="yellow")
button9.pack()
button0=Button(text="0",height=1,width=1,bg="black",fg="yellow")
button0.pack()



window.mainloop()


