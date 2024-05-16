import tkinter as tk
from tkinter import scrolledtext

class StudentResultManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Result Management System")
        self.root.geometry("350x450")  # Set the height and width here
        
        # Set the background color to black
        self.root.configure(bg="black")

        # Create a Frame for the notes section
        self.notes_frame = tk.Frame(self.root, bg="black")
        self.notes_frame.pack(fill=tk.BOTH, expand=True)

        # Create a Canvas widget for double buffering
        self.canvas = tk.Canvas(self.notes_frame, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Create a Text widget for displaying notes
        self.notes_text = scrolledtext.ScrolledText(self.canvas, wrap=tk.WORD, height=10, bg="black", fg="white")
        self.notes_text.pack(fill=tk.BOTH, expand=True)

        # Create an Entry widget for adding new notes
        self.note_entry = scrolledtext.ScrolledText(self.canvas, wrap=tk.WORD, height=5, bg="black", fg="white")
        self.note_entry.insert(tk.INSERT, "Add your note here")
        self.note_entry.bind("<Button-1>", self.clear_title)
        self.note_entry.pack(fill=tk.BOTH, expand=False)

        # Create an "Add Note" button
        self.add_note_button = tk.Button(self.canvas, text="Add Note", command=self.add_note, bg="black", fg="white")
        self.add_note_button.pack(fill=tk.BOTH, expand=False)

    def clear_title(self, event):
        if self.note_entry.get("1.0", tk.END) == "Add your note here\n":
            self.note_entry.delete("1.0", tk.END)

    def add_note(self):
        note = self.note_entry.get("1.0", tk.END)
        self.notes_text.insert(tk.END, note)
        self.note_entry.delete("1.0", tk.END)

    def run(self):
        self.root.mainloop()

# Create an instance of the class and run the application
if __name__ == "__main__":
    app = StudentResultManagementSystem()
    app.run()
