import tkinter as tk
from PIL import Image, ImageTk

SREEN_WIDTH = 600
SCREEN_HEIGHT = 700

root = tk.Tk()
root.geometry(str(SREEN_WIDTH) +"x"+ str(SCREEN_HEIGHT))
frame = tk.Frame()
frame.master.title("Skyfall")
canvas = tk.Canvas(frame)


canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()