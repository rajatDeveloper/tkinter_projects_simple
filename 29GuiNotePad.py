from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import  asksaveasfilename,askopenfilename
import os
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

def newFile():
    global file
    root.title("Untitled--NoteNow")
    file = None
    textArea.delete(1.0,END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file = None
    else :
        root.title(f"{os.path.basename} -- NoteNow ")
        textArea.delete(1.0,END)
        f = open(file,"r")
        textArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="untitled_text",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file = None
        else:
            f = open(file,"w")
            f.write(textArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+ "- NoteNow")   
    else: 
        f = open(file, "w")
        f.os.write(textArea.get(1.0, END))
        f.close()
def exitFile():
    pass
def cutFile():
    textArea.event_generate(("<<Cut>>"))
def copyFile():
    textArea.event_generate(("<<Copy>>"))
def pasteFile():
    textArea.event_generate(("<<Paste>>"))
def about():
    tmsg.showinfo("About","Note Now v2\nBy Rd Software")
canvas_width = 800
canvas_height = 400
root.minsize(222, 222)
root.title("Note Now")
# new_root.maxsize(666,666)

var_label_rd = Label(text="Note Now", bg="black",fg="white")
var_label_rd.pack(fill=X)
root.geometry(f"{canvas_width}x{canvas_height}")
# menu in gui non drop down
# mymenu = Menu(root)
# mymenu.add_command(label="Help", command=saveFun)
# mymenu.add_command(label="Update", command=updateFun)
# mymenu.add_command(label="Rate us", command=rateUs)
# mymenu.add_command(label="Quit", command=quit)
# root.config(menu=mymenu)
menuBar = Menu(root)
FileMenu = Menu(menuBar,tearoff=0,bg="grey")
FileMenu.add_command(label="New",command=newFile)
FileMenu.add_command(label="Open",command=openFile)
FileMenu.add_command(label="Save",command=saveFile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit",command=root.destroy)
menuBar.add_cascade(label="File", menu=FileMenu)

editmenu = Menu(menuBar,tearoff=0,bg="grey")
editmenu.add_command(label="Cut",command=cutFile)
editmenu.add_command(label="Copy",command=copyFile)
editmenu.add_command(label="Paste",command=pasteFile)
menuBar.add_cascade(label="Edit",menu=editmenu)

menuBar.add_command(label="Help", command=saveFun)
menuBar.add_command(label="Update", command=updateFun)
menuBar.add_command(label="Rate us", command=rateUs)
menuBar.add_command(label="About", command=about)
root.config(menu=menuBar)

scrolbar = Scrollbar()
scrolbar.pack(side=RIGHT, fill=Y)
textArea = Text(bg="grey",fg="black",height=1000,font="lucida 15", yscrollcommand=scrolbar.set)
textArea.pack(fill=BOTH)
file = None
scrolbar.config(command=textArea.yview)
# textArea.config(yscrollcommand=scrolbar.set)
root.mainloop()
