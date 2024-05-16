from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
import os
import re
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+50+50")
        self.root.config(bg="white")
        # ----------bg Images--------------
        self.bg_img=Image.open("img/reg_bg2.jpg")
        self.bg_img=self.bg_img.resize((1360,720))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img,bd=0).place(x=340,y=0)
        
        # ----------left Images--------------
        self.left=ImageTk.PhotoImage(file="img/side2.jpg")
        left=Label(self.root,image=self.left,text='Student Result \n Management System',compound='center',fg='white',font=("High Tower Text",26,"bold"),highlightbackground="darkgreen", highlightthickness=5).place(x=80,y=100,width=400,height=500)
        

        # --------Register Frame--------------
        frame1=Frame(self.root,bg="white",borderwidth=5,highlightbackground="darkgreen", highlightthickness=5)
        frame1.place(x=480,y=100,width=700,height=500)
        
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
# ------------------ 1      # 
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
            
        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)
# -----------------------------2
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)
            
            
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
        self.txt_email.bind("<FocusOut>", self.on_email_entry_change)

        self.email_validation_label = Label(frame1, text="", fg="black",bg="white")
        self.email_validation_label.place(x=550, y=175)
        
        
         
# -----------------------------3
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify='center')
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)    
            
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250) 
# -----------------------------4
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray",show='*')
        self.txt_password.place(x=50,y=340,width=250)
            
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray",show='*')
        self.txt_cpassword.place(x=370,y=340,width=250) 
# -----------------------------T&C
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree the Terms & Conditions.",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",12),bg="white").place(x=50,y=380)

        self.btn_img=ImageTk.PhotoImage(file="img/reg.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",bg="white",activebackground="white",command=self.register_data).place(x=50,y=420,height=60,width=150)
        
        btn_login=Button(self.root,text="LOG IN",command=self.login_window,font=("times new roman",20),bd=0,borderwidth=0,cursor="hand2",bg="white",fg="black",relief='raised',activebackground="white").place(x=200,y=470,width=180)
        
        
        # srms=Label(self.root,text="Student Result \n Management System",font=("times new roman",15,"bold")).place(x=200,y=310)
        
    def validate_email(self, email):
        # Regular expression to validate an email address
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, email))

    def on_email_entry_change(self, event):
        email = self.txt_email.get()
        if self.validate_email(email):
            self.email_validation_label.config(text="Valid Email", fg="green")
        else:
            self.email_validation_label.config(text="Invalid Email", fg="red")
            
#     ------------------------------------------------------------------------------------
    
    
    def login_window(self):
            self.root.destroy()
            os.system("python login.py")
    
    def clear(self):
            self.txt_fname.delete(0,END)
            self.txt_lname.delete(0,END)
            self.txt_contact.delete(0,END)
            self.txt_email.delete(0,END)
            self.txt_answer.delete(0,END)
            self.txt_password.delete(0,END)
            self.txt_cpassword.delete(0,END)
            self.cmb_quest.current(0)
    
    def register_data(self):
            valid=re.match("^[0-9]*$", self.txt_contact.get())
            if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
                messagebox.showerror("Error","All fields required",parent=self.root)
            elif self.txt_password.get()!=self.txt_cpassword.get():
                messagebox.showerror("Error","Password should be Same",parent=self.root)
            elif self.var_chk.get()==0:
                messagebox.showerror("Error","Plaease Agree our Terms & conditions",parent=self.root)
            elif not self.txt_fname.get().isalpha():
                messagebox.showerror("Error","Names should have alphabets only",parent=self.root)
            elif not self.txt_lname.get().isalpha():
                messagebox.showerror("Error","Names should have alphabets only",parent=self.root)
            elif not self.txt_contact.get().isdigit():
                messagebox.showerror("Error","Contact should have numbers only",parent=self.root)
            elif self.txt_contact.get()!=valid and len(self.txt_contact.get()) != 10:
                messagebox.showerror("Error","Contact must have 10 digits" ,parent=self.root)            
            elif self.email_validation_label.cget("text")=="Invalid Email":
                messagebox.showerror("Error","Invalid Email",parent=self.root)    
            else:
                try:
                    con=sqlite3.connect(database="srms.db")
                    cur=con.cursor()
                    cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                    row=cur.fetchone()
                    if row!=None:
                            messagebox.showerror("Error","User already exists",parent=self.root)
                    else:        
                        cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values (?,?,?,?,?,?,?)",
                                (self.txt_fname.get(),
                                        self.txt_lname.get(),
                                        self.txt_contact.get(),
                                        self.txt_email.get(),
                                        self.cmb_quest.get(),
                                        self.txt_answer.get(),
                                        self.txt_password.get()    
                                ))
                        con.commit()
                        con.close()  
                        messagebox.showinfo("Success","Registration Successfull",parent=self.root)
                        self.clear() 
                        self.login_window()       
                except Exception as es:
                        messagebox.showerror("Error",f"Error due to : {str(es)}",parent=self.root)
                            
                        
                                
                        
                      
            
               
root=Tk()
obj=Register(root)
root.mainloop()