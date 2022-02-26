from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()


def saveFun():
    print("i am save function")
    showinfo = tmsg.showinfo(
        "Help", "pls snd us your problem as email on rajatdelldhiman@gmail.com")


def rateUs():
    value = tmsg.askquestion("Was your experince Good?",
                             "U used this Gui ... was your experince good?")
    if value == 'yes':
        msg = "Great ... rate us on playStore"
    else:
        msg = "Tell your problem on \nrajatdelldhiman@gmail.com"
    tmsg.showinfo("Experience", msg)


def updateFun():
    ans = tmsg.askretrycancel("Upadte", "Checking for updates.......")
    if ans:
        tmsg.showinfo("Upadte Now", "Version 67.0")
    else:
        tmsg.showinfo("Upadte Cancel", "error as update is canceled ")


def click(event):
    # way to get the val by click
    text = event.widget.cget("text")
    print(f"{text} is number")
    # scValue.set(text)
    if text == "=":
        if scValue.get().isdigit():
            value = int(scValue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"

        scValue.set(value)
        screen.update()
    elif text == "C":
        scValue.set("")
        screen.update()
    else:
        scValue.set(scValue.get() + text)
        screen.update()


root.minsize(490, 598)
root.title("Calculate Now")
root.maxsize(490, 598)

var_label_rd = Label(text="Calcualate Now", bg="grey")
var_label_rd.pack(fill=X, pady=4)
root.geometry(f"490x598")
# menu in gui non drop down
mymenu = Menu(root)
mymenu.add_command(label="Help", command=saveFun)
mymenu.add_command(label="Update", command=updateFun)
mymenu.add_command(label="Rate us", command=rateUs)
mymenu.add_command(label="Quit", command=quit)
root.config(menu=mymenu)

# root.wm_iconbitmap("1.jpg")

# cal
scValue = StringVar()
scValue.set("")
screen = Entry(root, bg="white", textvariable=scValue, background="grey",
               font="lucida 22 bold",)
screen.pack(fill=X, pady=4, padx=2, ipady=22)
# screen1 = Entry(root, bg="white", textvariable=eqqValue,background="grey",
#                font="lucida 22 bold").pack(fill=X,pady=4,padx=2)

frame1 = Frame(root, bg="black")
button = Button(frame1, text="7", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
button = Button(frame1, text="8", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
button = Button(frame1, text="9", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
button = Button(frame1, text="*", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
frame1.pack()

frame2 = Frame(root, bg="black")
button = Button(frame2, text="4", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
button = Button(frame2, text="5", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
button = Button(frame2, text="6", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
button = Button(frame2, text="-", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
frame2.pack()

frame3 = Frame(root, bg="black")
button = Button(frame3, text="1", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
button = Button(frame3, text="2", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
button = Button(frame3, text="3", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
button = Button(frame3, text="+", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
frame3.pack()


frame4 = Frame(root, bg="black")
button = Button(frame4, text="%", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
button = Button(frame4, text="0", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
button = Button(frame4, text=".", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
button = Button(frame4, text="/", bg="grey",
                font="lucida 33 bold", height=1, width=4)
button.pack(side=LEFT, padx=2, pady=3)
button.bind("<Button-1>", click)
frame4.pack()

frame5 = Frame(root, bg="black")
button = Button(frame5, text="C", bg="grey",
                font="lucida 33 bold", height=1, width=8)
button.pack(side=LEFT, padx=2, pady=3, ipadx=6)
button.bind("<Button-1>", click)

button = Button(frame5, text="=", bg="grey",
                font="lucida 33 bold", height=1, width=8)
button.pack(side=LEFT, padx=2, pady=3, ipadx=6)
button.bind("<Button-1>", click)
frame5.pack()
root.configure(background="black")


root.mainloop()
