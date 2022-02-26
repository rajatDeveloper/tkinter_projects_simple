from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox as msg

class Student():
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title = "Student Management System"
        
        imageshow = Image.open(r"image/rd.jpg")
        imageshow = imageshow.resize((420, 160), Image.ANTIALIAS)
        self.photoImage =ImageTk.PhotoImage(imageshow)

        self.btn = Button(self.root,image=self.photoImage,cursor="hand2")
        self.btn.place(x=0,y=0,width=420,height=160)
# -----------------
        imageshow_2 = Image.open(r"image/rd.jpg")
        imageshow_2 = imageshow_2.resize((420, 160), Image.ANTIALIAS)
        self.photoImage_2 = ImageTk.PhotoImage(imageshow_2)

        self.btn_2 = Button(self.root, image=self.photoImage_2, cursor="hand2")
        self.btn_2.place(x=480, y=0, width=420, height=160)
# ------------------
        imageshow_3 = Image.open(r"image/rd.jpg")
        imageshow_3 = imageshow_3.resize((420, 160), Image.ANTIALIAS)
        self.photoImage_3 = ImageTk.PhotoImage(imageshow_3)

        self.btn_3 = Button(self.root, image=self.photoImage_3, cursor="hand2")
        self.btn_3.place(x=960, y=0, width=420, height=160)

        # bg image
        imageshow_bg = Image.open(r"image/notes.jpg")
        imageshow_bg = imageshow_bg.resize((1357,573), Image.ANTIALIAS)
        self.photoImage_bg = ImageTk.PhotoImage(imageshow_bg)
        bg_label = Label(self.root, image=self.photoImage_bg,bd=2,relief=RIDGE)
        bg_label.place(x=0,y=160,height=573,width=1357)
# ----------
        lb_title = Label(bg_label,text="Student Management System",font=("times new roman",37,"bold"),fg="white",bg="black")
        lb_title.place(x=0, y=0, width=1366,height=55)
        manage_frame = Frame(bg_label,relief=RIDGE,bg="white")
        manage_frame.place(x=15,y=55,width=1328,height=515)

# ----------
        # leftframe
        dataLeftFrame = LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,bg="black",fg="red",font=("times new roman",12,"bold"),text="Student Information")
        dataLeftFrame.place(x=10,y=10,width=540,height=500)

        imageshow_leftFrame = Image.open(r"image/rd.jpg")
        imageshow_leftFrame = imageshow_leftFrame.resize((540, 90), Image.ANTIALIAS)
        self.photoImage_leftFrame = ImageTk.PhotoImage(imageshow_leftFrame)

        self.btn_leftFrame = Button(dataLeftFrame, image=self.photoImage_leftFrame, cursor="hand2")
        self.btn_leftFrame.place(x=0, y=0, width=525, height=90)
        # cousreFrame
        datacourseFrame = LabelFrame(dataLeftFrame,bd=4,relief=RIDGE,padx=2,bg="black",fg="red",font=("times new roman",10,"bold"),text="Course Information")
        datacourseFrame.place(x=0,y=91,width=525,height=110)
        #label for dep
        lab_dep = Label(datacourseFrame, text="Department", fg="white", bg="black",font=("times new roman",10,"bold"))
        lab_dep.grid(row=0,column=0,padx=0,sticky=W)
        # dep var 
        self.var_dep = StringVar()
        combo_dep = ttk.Combobox(datacourseFrame,textvariable=self.var_dep,font=("times new roman",9,"bold"),width=20,state="readonly")
        combo_dep["value"]=("Select Deapartment","CSE","Civil","Mech","EC")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=12,pady=10,sticky=W)
 
        # couse
        lab_cor = Label(datacourseFrame, text="Course", fg="white", bg="black",font=("times new roman",10,"bold"))
        lab_cor.grid(row=1,column=0,padx=0,sticky=W)
        # var cor
        self.var_cor = StringVar()
        combo_cor = ttk.Combobox(datacourseFrame,textvariable=self.var_cor,font=("times new roman",9,"bold"),width=20,state="readonly")
        combo_cor["value"]=("Select Course","CSE 4yr","CSE 3yr LEET","Mech 4yr","Mech 3yr LEET")
        combo_cor.current(0)
        combo_cor.grid(row=1,column=1,padx=12,pady=10,sticky=W)

        # sem
        lab_sem = Label(datacourseFrame, text="Semster", fg="white", bg="black",font=("times new roman",10,"bold"))
        lab_sem.grid(row=0,column=3,padx=0,sticky=W)
        # var sem 
        self.var_sem = StringVar()
        combo_sem = ttk.Combobox(datacourseFrame,textvariable=self.var_sem,font=("times new roman",9,"bold"),width=20,state="readonly")
        combo_sem["value"]=("Select Sem","1 Sem","2 Sem","3 Sem","4 Sem","5 Sem","6 Sem","7 Sem","8 Sem")
        combo_sem.current(0)
        combo_sem.grid(row=0,column=4,padx=12,pady=10,sticky=W)
        # year 
        lab_yr = Label(datacourseFrame, text="Year", fg="white", bg="black",font=("times new roman",10,"bold"))
        lab_yr.grid(row=1,column=3,padx=0,sticky=W)
        # var yr 
        self.var_yr = StringVar()
        combo_yr = ttk.Combobox(datacourseFrame,textvariable=self.var_yr,font=("times new roman",9,"bold"),width=20,state="readonly")
        combo_yr["value"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        combo_yr.current(0)
        combo_yr.grid(row=1,column=4,padx=12,pady=10,sticky=W)

# std info Frame
        dataStdFrame = LabelFrame(dataLeftFrame,bd=4,relief=RIDGE,padx=2,bg="black",fg="red",font=("times new roman",10,"bold"),text="Student Data")
        dataStdFrame.place(x=0,y=200,width=525,height=240)
# -----LABEL std id
        lab_stdId = Label(dataStdFrame, text="Student Id ", fg="white", bg="black",font=("times new roman",10,"bold"))
        lab_stdId.grid(row=0,column=0,padx=10,sticky=W,pady=10)
# var id 
        self.var_id = StringVar()
        id_entry=ttk.Entry(dataStdFrame,textvariable=self.var_id,font=("arial",11,"bold"),width=18)
        id_entry.grid(row=0, column=1, padx=0, sticky=W,pady=10)
# -------- roll no . 
        lab_roll = Label(dataStdFrame, text="Roll no. ", fg="white", bg="black",font=("times new roman",10,"bold"))
        lab_roll.grid(row=0,column=2,padx=10,sticky=W,pady=10)
        # var roll no
        self.var_roll = StringVar()
        roll_entry=ttk.Entry(dataStdFrame,textvariable=self.var_roll,font=("arial",11,"bold"),width=18)
        roll_entry.grid(row=0, column=3, padx=0, sticky=W,pady=10)

# -----LABEL name
        lab_name = Label(dataStdFrame, text="Name ", fg="white", bg="black",font=("times new roman",10,"bold"))
        lab_name.grid(row=1,column=0,padx=10,sticky=W,pady=10)
# var name 
        self.var_name = StringVar()
        name_entry=ttk.Entry(dataStdFrame,textvariable=self.var_name,font=("arial",11,"bold"),width=18)
        name_entry.grid(row=1, column=1, padx=0, sticky=W,pady=10)
# --------email 
        lab_Email = Label(dataStdFrame, text="Email Id ", fg="white", bg="black",font=("times new roman",10,"bold"))
        lab_Email.grid(row=1,column=2,padx=10,sticky=W,pady=10)
        # var emial
        self.var_email = StringVar()
        email_entry=ttk.Entry(dataStdFrame,textvariable=self.var_email,font=("arial",11,"bold"),width=18)
        email_entry.grid(row=1, column=3, padx=0, sticky=W,pady=10)
        # ------gender
        lab_gender = Label(dataStdFrame, text="Gender ", fg="white", bg="black",font=("times new roman",10,"bold"))
        lab_gender.grid(row=2, column=0, padx=10, sticky=W, pady=10,)
        # var gender
        self.var_gen = StringVar()
        combo_gender = ttk.Combobox(dataStdFrame,textvariable=self.var_gen,font=("times new roman",9,"bold"),width=20,state="readonly")
        combo_gender["value"]=("Select Gender","Male","Female")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1,padx=5,pady=10,sticky=W)
        # ------phone
        lab_phn = Label(dataStdFrame, text="Phone No. ", fg="white", bg="black",font=("times new roman",10,"bold"))
        lab_phn.grid(row=2,column=2,padx=10,sticky=W,pady=10)
        # phn var 
        self.var_phn = StringVar()
        phn_entry=ttk.Entry(dataStdFrame,textvariable=self.var_phn,font=("arial",11,"bold"),width=18)
        phn_entry.grid(row=2, column=3, padx=0, sticky=W,pady=10)



# -----LABEL Dob
        lab_dob = Label(dataStdFrame, text="DOB ", fg="white", bg="black",font=("times new roman",10,"bold"))
        lab_dob.grid(row=3, column=0, padx=10, sticky=W, pady=10)
# dob var 
        self.var_dob = StringVar()
        dob_entry=ttk.Entry(dataStdFrame,textvariable=self.var_dob,font=("arial",11,"bold"),width=18)
        dob_entry.grid(row=3, column=1, padx=0, sticky=W,pady=10)
# --------Caste 
        lab_Caste = Label(dataStdFrame, text="Caste ", fg="white", bg="black",font=("times new roman",10,"bold"))
        lab_Caste.grid(row=3,column=2,padx=10,sticky=W,pady=10)
        # var catse 
        self.var_caste = StringVar()
        combo_gender = ttk.Combobox(dataStdFrame,textvariable=self.var_caste,font=("times new roman",9,"bold"),width=20,state="readonly")
        combo_gender["value"]=("Select Caste","Gernal","OBC","SC/ST")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=3,padx=5,pady=10,sticky=W)

        # -------------address
        lab_Address = Label(dataStdFrame, text="Address ", fg="white", bg="black",font=("times new roman",10,"bold"))
        lab_Address.grid(row=4,column=0,padx=10,sticky=W,pady=10)
        # var address
        self.var_address = StringVar()
        address_entry = ttk.Entry(dataStdFrame,textvariable=self.var_address, font=("arial", 11, "bold"), width=18)
        address_entry.grid(row=4, column=1, padx=0, sticky=W, pady=10)
        # -------------Father name
        lab_Father = Label(dataStdFrame, text="Father Name ", fg="white", bg="black",font=("times new roman",10,"bold"))
        lab_Father.grid(row=4,column=2,padx=10,sticky=W,pady=10)
# var father 
        self.var_father = StringVar()
        father_entry = ttk.Entry(dataStdFrame,textvariable=self.var_father,font=("arial", 11, "bold"), width=18)
        father_entry.grid(row=4, column=3, padx=0, sticky=W, pady=10)

        # --------------------btn frame width=540,height=500)
        btn_frame = Frame(dataLeftFrame, relief=RIDGE, bg="grey")
        btn_frame.place(x=0, y=444, width=524, height=28)

        # btn 
        btn_AddData = Button(btn_frame,bg="red",text="Add",width=17,command=self.addData)
        btn_AddData.grid(row=0,column=1,padx=1)

        btn_Update = Button(btn_frame, bg="red", text="Update", width=17)
        btn_Update.grid(row=0, column=2,padx=1)

        btn_del = Button(btn_frame,bg="red",text="Delete",width=17)
        btn_del.grid(row=0,column=3,padx=1)

        btn_reset = Button(btn_frame,bg="red",text="Reset",width=17)
        btn_reset.grid(row=0,column=4,padx=1)


# -----------------------------------------

        # right frame 
        dataRightFrame = LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,bg="black",fg="red",font=("times new roman",12,"bold"),text="Student Data")
        dataRightFrame.place(x=560,y=10,width=759,height=500)

        imageshow_rightFrame = Image.open(r"image/rd.jpg")
        imageshow_rightFrame = imageshow_rightFrame.resize((759, 90), Image.ANTIALIAS)
        self.photoImage_rightFrame = ImageTk.PhotoImage(imageshow_rightFrame)

        self.btn_rightFrame = Button(dataRightFrame, image=self.photoImage_leftFrame, cursor="hand2")
        self.btn_rightFrame.place(x=0, y=0, width=750, height=90)

        # -------------- search 
        SerachFrame = LabelFrame(dataRightFrame,bd=4,relief=RIDGE,padx=2,bg="black",fg="red",font=("times new roman",12,"bold"),text="Search Now")
        SerachFrame.place(x=0,y=92,width=749,height=60)

        lab_Search = Label(SerachFrame, text="Search By ", fg="white", bg="black",font=("times new roman",12,"bold"))
        lab_Search.grid(row=0,column=0,padx=10,sticky=W,pady=2)

        combo_search = ttk.Combobox(SerachFrame,font=("times new roman",9,"bold"),width=20,state="readonly")
        combo_search["value"]=("Select Option","Roll no.","Phone no.","Student Id")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=5,pady=2,sticky=W)

        # search_entry = StringVar
        search_entry = ttk.Entry(SerachFrame, font=("arial", 11, "bold"), width=25)
        search_entry.grid(row=0, column=2, padx=5, sticky=W, pady=2)
# serach
        btn_Search = Button(SerachFrame, bg="red", text="Search", width=17)
        btn_Search.grid(row=0, column=3,padx=1)
# update 
        btn_ShowData = Button(SerachFrame, bg="red", text="Show Data", width=17)
        btn_ShowData.grid(row=0, column=4, padx=1,pady=2)
# table std and scroll bar 
        tableFrame = LabelFrame(dataRightFrame,bd=4,relief=RIDGE,padx=2,bg="black",fg="red",font=("times new roman",12,"bold"),text="All Saved Data ")
        tableFrame.place(x=0,y=152,width=749,height=321)

        # scrollbar 
        # scrolBarData = Scrollbar(tableFrame,orient=HORIZONTAL)
        scroll_x= ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(tableFrame,orient=VERTICAL)
        self.studentTable = ttk.Treeview(tableFrame,columns=("dep","sem","course","yr","id","roll","name","email","gender","phn","dob","caste","address","fth"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.studentTable.xview)
        scroll_y.config(command=self.studentTable.yview)
        # "dep","sem","course","yr","id","roll","name","email",
        # "gender","phn","dob","caste","address","fth"
        self.studentTable.heading("dep",text="Department")
        self.studentTable.heading("sem",text="Semester")
        self.studentTable.heading("course",text="Course")
        self.studentTable.heading("yr",text="Year")
        self.studentTable.heading("id",text="Student Id")
        self.studentTable.heading("roll",text="Roll no.")
        self.studentTable.heading("name",text="Name")
        self.studentTable.heading("email",text="Email Id")
        self.studentTable.heading("gender",text="Gender")
        self.studentTable.heading("phn",text="Phone no.")
        self.studentTable.heading("dob",text="DOB")
        self.studentTable.heading("caste",text="Caste")
        self.studentTable.heading("address",text="Address")
        self.studentTable.heading("fth",text="Father Name")
        self.studentTable["show"]="headings"


        self.studentTable.pack(fill=BOTH,expand=1) 

    def addData(self):
        # if (self.var_dep.get()or self.var_id.get()or self.var_roll.get()):
        #         msg.showerror("Error","Field should be filled ")
        # else: 

        try :
                conn = mysql.connector.connect(host="localhost",username="root",password="Rajat@12345",database="student")
                my_cursur = conn.cursor()
                my_cursur =  execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                        self.var_dep.get(),
                        self.var_sem.get(),
                        self.var_cor.get(),
                        self.var_yr.get(),
                        self.var_id.get(),
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gen.get(),
                        self.var_phn.get(),
                        self.var_dob.get(),
                        self.var_caste.et(),
                        self.var_address.get(),
                        self.var_father.get(),
                ))
                conn.commit()
                conn.close
                msg.showinfo("Data","Student Data is stored in Database successfully",parent=self.root)
        except Exception as ex : 
                msg.showerror("Error",f"Try again , error is due to {str(ex)}",parent=self.root)




if __name__ =="__main__":
    root = Tk()
    
    obj = Student(root)

   

    root.mainloop()





