from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk, ImageDraw
import os


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+50+50")
        self.root.config(bg="#021e2f")

        # ---------------BG---------------------------------
        self.bg_img = Image.open("img/reg_bg2.jpg")
        self.bg_img = self.bg_img.resize((1360, 720))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img, bd=0).place(x=479, y=0)

        left_lbl = Label(self.root, bg='white', bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=479)



        # left_lbl = Label(self.root, bg='#08A3D2', bd=0)
        # left_lbl.place(x=0, y=0, relheight=1, width=479)
        #
        # right_lbl = Label(self.root, bg='#031F3C', bd=0)
        # right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        self.left = ImageTk.PhotoImage(file="img/reg_bg2.jpg")
        left = Label(self.root, image=self.left, text='Student Result \n Management System', compound='center',
                     fg='white', font=("High Tower Text", 28, "bold"),borderwidth=5,highlightbackground="darkgreen", highlightthickness=5).place(x=80, y=100, width=400, height=500)

        # --------------frames---------------------------------
        login_frame = Frame(self.root, bg='white',borderwidth=5,highlightbackground="darkgreen", highlightthickness=5 )
        login_frame.place(x=480, y=100, width=600, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 28, "bold"), bg="white",
                      fg="green").place(x=60, y=50)
        # ------------------------------------------------------------
        email = Label(login_frame, text="EMAIL ADDRESS", font=("times new roman", 18, "bold"), bg="white",
                      fg="gray").place(x=60, y=150)
        self.txt_email = Entry(login_frame, font=("times new roman", 18), bg="lightgray", highlightbackground="black",
                               highlightcolor="black", highlightthickness=1)
        self.txt_email.place(x=60, y=180, width=350, height=35)

        passs = Label(login_frame, text="PASSWORD", font=("times new roman", 18, "bold"), bg="white", fg="gray").place(
            x=60, y=250)
        self.txt_passs = Entry(login_frame, font=("times new roman", 18), bg="lightgray", show="*",
                               highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.txt_passs.place(x=60, y=280, width=350, height=35)

        btn_reg = Button(login_frame, text="Register new Faculty ?", command=self.reg_window,
                         font=("times new roman", 14), bg='white', bd=0, fg='#B00857', cursor='hand2').place(x=60,
                                                                                                             y=320)
        btn_forget = Button(login_frame, text="Forget Password ?", command=self.forget_pass_window,
                            font=("times new roman", 14), bg='white', bd=0, fg='red', cursor='hand2').place(x=260,
                                                                                                            y=320)

        btn_login = Button(login_frame, text="Login", font=("times new roman", 20, "bold"), fg='white', bg='#B00857',
                           cursor='hand2', command=self.login).place(x=60, y=380, width=180, height=40)

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_passs.delete(0, END)
        self.txt_email.delete(0, END)

    def forget_pass(self):
        if self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_new_pass.get() == "":
            messagebox.showerror("Error", "All Fields required..", parent=self.root2)
        else:
            try:
                con = sqlite3.connect(database="srms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=? ",
                            (self.txt_email.get(), self.cmb_quest.get(), self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select correct Security Question / Enter correct Answer ",
                                         parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=? ",
                                (self.txt_new_pass.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success",
                                        "Your password has been reset successfully,\n Please login with new password",
                                        parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except EXCEPTION as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=self.root)

    def forget_pass_window(self):
        if self.txt_email.get() == "":
            messagebox.showerror("Error", "Please enter email address to reset your password", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="srms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? ", (self.txt_email.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please enter valid email address to reset your password",
                                         parent=self.root)
                else:
                    con.close()
                    self.forpass()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=self.root)

    def forpass(self):
        self.root2 = Toplevel()
        self.root2.title("Forget Password")
        self.root2.geometry("400x400+550+200")
        self.root2.config(bg='white')
        self.root2.focus_force()
        self.root2.grab_set()

        title = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), bg='white',
                      fg='red').place(x=0, y=10, relwidth=1)

        # -----------------------------fg passs
        question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), bg="white",
                         fg="gray").place(x=80, y=100)

        self.cmb_quest = ttk.Combobox(self.root2, font=("times new roman", 13), state='readonly', justify='center')
        self.cmb_quest['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
        self.cmb_quest.place(x=80, y=130, width=250)
        self.cmb_quest.current(0)

        answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=80, y=180)
        self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=80, y=210, width=250)

        new_pass = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white",
                         fg="gray").place(x=80, y=260)
        self.txt_new_pass = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
        self.txt_new_pass.place(x=80, y=290, width=250)

        btn_change_pass = Button(self.root2, text="Reset Password", command=self.forget_pass, bg='green', fg='white',
                                 font=("times new roman", 15, "bold")).place(x=130, y=340)

    def reg_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get() == "" or self.txt_passs.get() == "":
            messagebox.showerror("Error", "All fields required", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="srms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and password=?",
                            (self.txt_email.get(), self.txt_passs.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Inavalid USERNAME & PASSWORD", parent=self.root)
                else:
                    txt=row[1]
                    messagebox.showinfo("Success", f"Welcome {txt.upper()}", parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=self.root)


root = Tk()
obj = Login_window(root)
root.mainloop()
