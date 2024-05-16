from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import re


class reportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1000x650+300+120")
        self.root.config(bg="white")
        self.root.focus_force()

        self.bg_img=Image.open("img/girl.jpg")
        self.bg_img=self.bg_img.resize((400,600))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img,bd=0).place(x=0,y=65)
        # ----------------------------------------------------------------------
        # self.bg2_img=Image.open("img/boy.jpg")
        # self.bg2_img=self.bg2_img.resize((400,600))
        # self.bg2_img=ImageTk.PhotoImage(self.bg2_img)

        # self.lbl_bg=Label(self.root,image=self.bg2_img,bd=0).place(x=850,y=65)

        # -----------------Title -----------------
        title = Label(self.root, text="View Student Results", font=("goudy old style", 20, "bold"), bg="#038074",
                      fg="white").place(x=10, y=15, width=980, height=40)

        # ------------search--------------------
        self.var_search = StringVar()
        self.roll_list = []
        self.fetch_roll()
        self.var_id = ""

        lbl_search = Label(self.root, text="Enter Roll No. ", font=("goudy old style", 20, "bold"), bg="white").place(
            x=450, y=100)

        # txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 20),
        #                    bg="lightyellow").place(x=630, y=100, width=150)

        self.txt_search = ttk.Combobox(self.root, textvariable=self.var_search, values=self.roll_list,
                                        font=("goudy old style", 17, 'bold'), justify=CENTER)
        self.txt_search.place(x=630, y=100, width=160)

    def fetch_roll(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            cur.execute("select roll from student")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.roll_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

        # ------------------------------------------
        btn_search = Button(self.root, text='Search', font=("goudy old style", 17, 'bold'), bg="#03a9f4", fg="white",
                            cursor="hand2", command=self.search).place(x=420, y=150, width=100, height=35)
        # ------------------------------------------
        btn_clear = Button(self.root, text='Clear', font=("goudy old style", 17, 'bold'), bg="gray", fg="white",
                           cursor="hand2", command=self.clear).place(x=530, y=150, width=100, height=35)

        # -----------------DELETE-------------------------
        btn_delete = Button(self.root, text='Delete', font=("goudy old style", 17, 'bold'), bg="Red", fg="white",
                            cursor="hand2", command=self.delete).place(x=640, y=150, width=150, height=35)

        # ------------labels----------
        lbl_roll = Label(self.root, text="Roll No", font=("goudy old style", 15, "bold"), bg="white", bd=2,
                         relief=GROOVE).place(x=350, y=230, width=250, height=50)

        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white", bd=2,
                         relief=GROOVE).place(x=350, y=285, width=250, height=50)

        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white", bd=2,
                           relief=GROOVE).place(x=350, y=340, width=250, height=50)

        lbl_marks = Label(self.root, text="Marks Obtained", font=("goudy old style", 15, "bold"), bg="white", bd=2,
                          relief=GROOVE).place(x=350, y=395, width=250, height=50)

        lbl_full = Label(self.root, text="Total Marks", font=("goudy old style", 15, "bold"), bg="white", bd=2,
                         relief=GROOVE).place(x=350, y=450, width=250, height=50)

        lbl_per = Label(self.root, text="Percentage", font=("goudy old style", 15, "bold"), bg="white", bd=2,
                        relief=GROOVE).place(x=350, y=505, width=250, height=50)

        # -----------------------------

        self.roll = Label(self.root, font=("goudy old style", 18, "bold"), bg="white", fg='green', bd=2, relief=GROOVE)
        self.roll.place(x=600, y=230, width=250, height=50)

        self.name = Label(self.root, font=("goudy old style", 18, "bold"), bg="white", fg='green', bd=2, relief=GROOVE)
        self.name.place(x=600, y=285, width=250, height=50)
        #
        self.course = Label(self.root, font=("goudy old style", 18, "bold"), bg="white", fg='green', bd=2,
                            relief=GROOVE)
        self.course.place(x=600, y=340, width=250, height=50)
        #
        self.marks = Label(self.root, font=("goudy old style", 18, "bold"), bg="white", fg='green', bd=2, relief=GROOVE)
        self.marks.place(x=600, y=395, width=250, height=50)
        #
        self.full = Label(self.root, font=("goudy old style", 18, "bold"), bg="white", fg='green', bd=2, relief=GROOVE)
        self.full.place(x=600, y=450, width=250, height=50)
        #
        self.per = Label(self.root, font=("goudy old style", 20, "bold"), bg="white", fg='green', bd=2, relief=GROOVE)
        self.per.place(x=600, y=505, width=250, height=50)
        #
        self.last = Label(self.root, font=("goudy old style", 20, "bold"),
                          bg="white", fg='green', bd=0, relief=GROOVE)
        self.last.place(x=500, y=575, height=50)

    # --------------------------------------------

    def search(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            valid = re.match("^[0-9]*$", self.var_search.get())
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Roll No. is required", parent=self.root)
            elif not self.var_search.get().isdigit():
                messagebox.showerror("Error", "Roll No. must be Numeric", parent=self.root)
            elif self.var_search.get() != valid and len(self.var_search.get()) != 3:
                messagebox.showerror("Error", "Roll No. must be of 3 digits", parent=self.root)
            else:
                cur.execute(f"select * from result where roll=?", (self.var_search.get(),))
                row = cur.fetchone()
                if row != None:
                    percentage = row[6]
                    self.var_id = row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])

                    if percentage < 33:
                        self.per.config(text=f"{(row[6])}%", fg='white',bg='red')
                        self.last.config(text=f"{(row[2])}, has Failed the exam", fg='red')
                    else:
                        self.per.config(text=f"{(row[6])}%", fg='white',bg='green')
                        self.last.config(text=f"{(row[2])}, has Passed the exam", fg='green')
                else:
                    messagebox.showerror("Error", "No Record found", parent=self.root)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_id = ""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="",bg='white')
        self.last.config(text="")
        self.var_search.set("")

    # -------------------------------------------------------------------------------

    def delete(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            if self.var_id == "":
                messagebox.showerror("Error", "Search student result first", parent=self.root)
            else:
                cur.execute("select * from result where rid=?", (self.var_id,))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Student result", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from result where rid=?", (self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete", "Result deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


# -----------------------------------------------
if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()
