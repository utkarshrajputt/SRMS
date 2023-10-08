import tkinter as tk

# Create a tkinter window
root = tk.Tk()
root.title("Simple Vertical Bar")

# Create a Canvas widget for the vertical bar
canvas = tk.Canvas(root, width=50, height=400)  # Adjust the width and height as needed
canvas.pack()

# Draw a vertical bar
canvas.create_rectangle(10, 40, 30, 350, fill="black")  # Adjust the coordinates and color as needed

# Run the tkinter main loop
root.mainloop()
