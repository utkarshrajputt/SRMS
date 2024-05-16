from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import datetime
import re

class studentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1400x480+70+200")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # -----------------Title -----------------
        title=Label(self.root,text="Manage Student Details",font=("goudy old style",20,"bold"),bg="#012542",fg="white").place(x=10,y=7,width=1380,height=40)
        
        # ------------------Variables-----------
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
        
        
        # ------------------Widgets------------
        
        # --------------------Column1------------
        lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=60)
        lbl_Name=Label(self.root,text="Name",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=100)
        lbl_Email=Label(self.root,text="Email",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=140)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=180)
        
        lbl_state=Label(self.root,text="State",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=330)
        txt_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=150,y=330,width=150)
        
        lbl_city=Label(self.root,text="City",font=("goudy old style",15,'bold'),bg='white').place(x=310,y=330)
        txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=360,y=330,width=140)
        
        lbl_pin=Label(self.root,text="Pin",font=("goudy old style",15,'bold'),bg='white').place(x=520,y=330)
        txt_pin=Entry(self.root,textvariable=self.var_pin,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=570,y=330,width=110)
        
        
        
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=220)
        
        # ---------------------Entry Fields-------------
        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_roll.place(x=150,y=60,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=150,y=100,width=200)
        
        
        self.txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_email.place(x=150,y=140,width=200)
        self.txt_email.bind("<FocusOut>", self.on_email_entry_change)

        self.email_validation_label = Label(self.root, text="", fg="black",bg="white")
        self.email_validation_label.place(x=250, y=560)
        
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Male","Female","Others"),font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
        self.txt_gender.place(x=150,y=180,width=200)
        self.txt_gender.set("Select")
        
        # --------------------Column2------------
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15,'bold'),bg='white').place(x=360,y=60)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,'bold'),bg='white').place(x=360,y=100)
        lbl_admission=Label(self.root,text="Admit Date",font=("goudy old style",15,'bold'),bg='white').place(x=360,y=140)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,'bold'),bg='white').place(x=360,y=180)
        
        # ---------------------Entry Fields 2-------------
        self.course_list=[]
        # function call to update list
        self.fetch_course()
        
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=480,y=60,width=200)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=480,y=100,width=200)
        txt_admission=Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=480,y=140,width=200)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
        self.txt_course.place(x=480,y=180,width=200)
        self.txt_course.set("Select")
        
        # ---------------txt address----------------
        self.txt_address=Text(self.root,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_address.place(x=150,y=220,width=530,height=100)
        
        # -------------------Buttons-------------------
        self.btn_add=Button(self.root,text='Save',font=("goudy old style",18,'bold'),bg="#2196f3",fg="black",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=100,height=50)
        
        self.btn_update=Button(self.root,text='Update',font=("goudy old style",18,'bold'),bg="#4caf50",fg="black",cursor="hand2",command=self.update)
        self.btn_update.place(x=260,y=400,width=100,height=50)
        
        self.btn_delete=Button(self.root,text='Delete',font=("goudy old style",18,'bold'),bg="#f44336",fg="black",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=370,y=400,width=100,height=50)
        
        self.btn_clear=Button(self.root,text='Clear',font=("goudy old style",18,'bold'),bg="#607d8b",fg="black",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=480,y=400,width=100,height=50)
        
        left_lbl = Label(self.root, bg='#012542', bd=0)
        left_lbl.place(x=690, y=48, relheight=1, width=20)
        
        # ------------Search Panel------------------------
        self.var_search=StringVar()
        lbl_search_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,'bold'),bg='white').place(x=720,y=60)
        txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=870,y=60,width=180)
        btn_search=Button(self.root,text='Search',font=("goudy old style",18,'bold'),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)
        
        # ------------Content---------------------------------
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=670,height=370)
        
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
                
        self.CourseTable.heading("roll",text="Roll No.")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="D.O.B")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("admission",text="Admission")
        self.CourseTable.heading("course",text="Course")
        
        self.CourseTable.heading("state",text="State")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("pin",text="PIN")
        self.CourseTable.heading("address",text="Address")
        
        
        
        self.CourseTable["show"]='headings'
        
        self.CourseTable.column("roll",width=50)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("email",width=150)
        self.CourseTable.column("gender",width=100)
        self.CourseTable.column("dob",width=100)
        self.CourseTable.column("contact",width=100)
        self.CourseTable.column("admission",width=100)
        self.CourseTable.column("course",width=100)
        self.CourseTable.column("state",width=100)
        self.CourseTable.column("city",width=100)
        self.CourseTable.column("pin",width=100)
        self.CourseTable.column("address",width=200)
        
        
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        

# ---------------------------------------------------------------------------

    def validate_email(self, email):
        # Regular expression
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, email))

    def on_email_entry_change(self, event):
        email = self.txt_email.get()
        if self.validate_email(email):
            self.email_validation_label.config(text="Valid Email", fg="green")
        else:
            self.email_validation_label.config(text="Invalid Email", fg="red")
# ---------------------------------------------------------------------------
    
    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0",END)
        self.txt_address.config(state=NORMAL)
        self.txt_roll.config(state="normal")
        self.var_search.set("")
        self.show()
        
        

# ---------------------------------------------------------------------------

    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[11])

# ---------------------------------------------------------------------------
    def add(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            valid=re.match("^[0-9]*$", self.var_contact.get())
            ex_len=10;
            date_format = '%d-%m-%Y'

            if self.var_roll.get()=="" or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="Select" or self.var_dob.get()=="" or self.var_contact.get()=="" or self.var_a_date.get()=="" or self.var_course.get()=="Select" or self.var_state.get()=="" or self.var_city.get()=="" or self.var_pin.get()=="" :
                messagebox.showerror("Error","All Fields are required",parent=self.root)
            elif not self.var_roll.get().isdigit():
                messagebox.showerror("Error","Roll No. should be a numeric value" ,parent=self.root)
            elif self.email_validation_label.cget("text")=="Invalid Email":
                messagebox.showerror("Error","Invalid Email",parent=self.root)
            elif not self.var_name.get().isalpha():
                messagebox.showerror("Error","Name should have alphabets only",parent=self.root)
            elif not self.var_contact.get().isdigit():
                messagebox.showerror("Error","Contact should have numbers only" ,parent=self.root)
            elif len(self.var_contact.get())!=ex_len:
                messagebox.showerror("Error","Contact should have 10 digits" ,parent=self.root)
            elif self.var_contact.get()!=valid and len(self.var_contact.get()) != 10:
                messagebox.showerror("Error","Contact must have 10 digits" ,parent=self.root)
            elif not self.var_state.get().isalpha():
                messagebox.showerror("Error","State name should have alphabets only",parent=self.root)
            elif not self.var_city.get().isalpha():
                messagebox.showerror("Error","City name should have alphabets only",parent=self.root)
            elif self.var_pin.get()!=valid and len(self.var_pin.get()) != 6:
                messagebox.showerror("Error","PIN must be of 6 digits" ,parent=self.root)
            else:
                Admit_dateObject = datetime.datetime.strptime(self.var_a_date.get(), date_format)
                dob_dateObject = datetime.datetime.strptime(self.var_dob.get(), date_format)
                cur.execute("select * from student where name=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll No. already present",parent=self.root)
                else:
                    cur.execute("insert into student (roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
# ---------------------------------------------------------------------------
    def update(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            # pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            # v_email=re.match(pattern, self.var_email.get())
            valid=re.match("^[0-9]*$", self.var_contact.get())
            ex_len=10;
            date_format = '%d-%m-%Y'
            Admit_dateObject = datetime.datetime.strptime(self.var_a_date.get(), date_format)
            dob_dateObject = datetime.datetime.strptime(self.var_dob.get(), date_format)
            if self.var_roll.get()=="" or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="Select" or self.var_dob.get()=="" or self.var_contact.get()=="" or self.var_a_date.get()=="" or self.var_course.get()=="Select" or self.var_state.get()=="" or self.var_city.get()=="" or self.var_pin.get()=="" :
                messagebox.showerror("Error","Enter the details",parent=self.root)
            elif self.email_validation_label.cget("text")=="Invalid Email":
                messagebox.showerror("Error","Invalid Email",parent=self.root)
            # elif self.var_email.get()!=v_email:
            #     messagebox.showerror("Error","Invalid Email",parent=self.root)
            elif not self.var_name.get().isalpha():
                messagebox.showerror("Error","Name should have alphabets only",parent=self.root)
            elif not self.var_contact.get().isdigit():
                messagebox.showerror("Error","Contact should have numbers only" ,parent=self.root)
            # elif len(self.var_contact.get())!=ex_len:
            #     messagebox.showerror("Error","Contact should have 10 digits" ,parent=self.root)
            elif self.var_contact.get()!=valid and len(self.var_contact.get()) != 10:
                messagebox.showerror("Error","Contact must have 10 digits" ,parent=self.root)
            elif not self.var_state.get().isalpha():
                messagebox.showerror("Error","State name should have alphabets only",parent=self.root)
            elif not self.var_city.get().isalpha():
                messagebox.showerror("Error","City name should have alphabets only",parent=self.root)
            elif self.var_pin.get()!=valid and len(self.var_pin.get()) != 6:
                messagebox.showerror("Error","PIN must be of 6 digits" ,parent=self.root)
            
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student from list",parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                        self.var_roll.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
# -------------------------------------------------------------------------------

    def delete(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. is required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        

# -------------------------------------------------------------------------------

    def show(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
# -------------------------------------------------------------------------------

    def fetch_course(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
# -----------------------------------------------
    
    def search(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. is required",parent=self.root)
            elif not self.var_search.get().isdigit():
                messagebox.showerror("Error","Roll No. must be Numeric",parent=self.root)
            else:
                cur.execute(f"select * from student where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.CourseTable.delete(*self.CourseTable.get_children())
                    self.CourseTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record found",parent=self.root)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

# -----------------------------------------------

if __name__=="__main__":
    root=Tk()
    obj=studentClass(root)
    root.mainloop()