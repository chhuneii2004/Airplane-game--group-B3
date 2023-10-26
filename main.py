import tkinter as tk
from PIL import Image, ImageTk

SREEN_WIDTH = 600
SCREEN_HEIGHT = 700
PLAYER_SPEED = 10
BULLET_SPEED = 7
ENEMY_SPEED = 1
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100
BULLET_WIDTH = 30
BULLET_HEIGHT = 40
ENEMY_WIDTH = 100
ENEMY_HEIGHT = 100
score = 0

root = tk.Tk()
root.geometry(str(SREEN_WIDTH) +"x"+ str(SCREEN_HEIGHT))
frame = tk.Frame()
frame.master.title("Skyfall")
canvas = tk.Canvas(frame)


canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()