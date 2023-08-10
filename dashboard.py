from tkinter import*
from PIL import Image,ImageTk
from course import CourseClass
from student import studentClass
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x750+50+20")
        self.root.config(bg="white")
        # ----------------Icons----------
        self.logo_dash=ImageTk.PhotoImage(file="img/analysis.png")


        # -----------------Title -----------------
        title=Label(self.root,text="Student Result Management System",padx=20,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        
        # -----------------Menu-------------
        M_Frame=LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1330,height=80)

        # -----------------Buttons--------------------
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=460,y=5,width=200,height=40)
        
        btn_view=Button(M_Frame,text="View Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=680,y=5,width=200,height=40)
        
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=900,y=5,width=200,height=40)
        
        btn_exit=Button(M_Frame,text="Exit",command=lambda:root.destroy(),font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1120,y=5,width=200,height=40)

        # ------------content-img--------------
        self.bg_img=Image.open("img/bg.jpg")
        self.bg_img=self.bg_img.resize((920,450))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=450)

        # -----------------update details---------------
        self.lbl_course=Label(self.root,text="Total Courses\n [ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=635,width=300,height=100)
        
        self.lbl_student=Label(self.root,text="Total Students\n [ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=635,width=300,height=100)
        
        self.lbl_result=Label(self.root,text="Total Results\n [ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=635,width=300,height=100)
    
    def add_course(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=CourseClass(self.new_win)        
    
    def add_student(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=studentClass(self.new_win)        


# -----------------------------------------------
if __name__=="__main__":
    root=Tk()
    # root.overrideredirect(True)
    obj=RMS(root)
    root.mainloop()