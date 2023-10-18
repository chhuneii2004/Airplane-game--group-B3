import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x6600")
frame = tk.Frame()
frame.master.title("Skyfall")
canvas = tk.Canvas(frame)

bg = Image.open("images/background.jpg")
image = ImageTk.PhotoImage(bg)
canvas.create_image(300,150, image=image)

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()