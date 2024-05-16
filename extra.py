import tkinter as tk
import re

class StudentResultApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")

        frame1 = tk.Frame(self.root, bd=2, relief=tk.RIDGE, bg="white")
        frame1.place(x=50, y=100, width=500, height=400)

        email_label = tk.Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        email_label.place(x=370, y=170)

        self.txt_email = tk.Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)
        self.txt_email.bind("<FocusOut>", self.on_email_entry_change)

        self.email_validation_label = tk.Label(frame1, text="", fg="black")
        self.email_validation_label.place(x=370, y=230)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentResultApp(root)
    root.mainloop()
