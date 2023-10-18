import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x900")
frame = tk.Frame()
frame.master.title("Skyfall")
canvas = tk.Canvas(frame)

bg = Image.open("images/starbackground.png")
image = ImageTk.PhotoImage(bg)
canvas.create_image(300,300, image=image)

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()