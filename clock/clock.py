from tkinter import *
from PIL import Image,ImageTk,ImageDraw
class Clock:
    def __init__(self,root):
        self.root=root
        self.root.title("Ananlog Clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        
        title=Label(self.root,text="Analog Clock",font=("times new roman",50,"bold"),bg="#04444a",fg="white").place(x=0,y=50,relwidth=1)
    
        self.lbl=Label(self.root,bg="white")
        self.lbl.place(x=450,y=150,height=400,width=400) 
        self.clock_image()
        
    def clock_image(self):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw=ImageDraw.Draw(clock)
        
        bg=Image.open("cl.jpg")
        bg=bg.resize((300,300))
        clock.paste(bg,(50,50))
        
        clock.save("clock_new.png")
        
root=Tk()
obj=Clock(root)
root.mainloop()