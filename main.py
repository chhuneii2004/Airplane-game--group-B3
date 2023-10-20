import tkinter as tk
from PIL import Image, ImageTk

SREEN_WIDTH = 600
SCREEN_HEIGHT = 700

root = tk.Tk()
root.geometry(str(SREEN_WIDTH) +"x"+ str(SCREEN_HEIGHT))
frame = tk.Frame()
frame.master.title("Skyfall")
canvas = tk.Canvas(frame)

#Insert image bg
bg_image = Image.open("images/starbackground.png")
bg_image = ImageTk.PhotoImage(bg_image)
canvas.create_image(300,300, image=bg_image)

#Creat player
f15 = Image.open("images/f15.png")
f15 = f15.resize((70,70))
f15 = ImageTk.PhotoImage(f15)
player = canvas.create_image(300,650, image=f15)

#creat shooting 


#move player
def move(event):
    if event.keysym == "Left" and canvas.coords(player)[0]>40:
        canvas.move(player,-10,0)
    elif event.keysym == "Right"and canvas.coords(player)[0]<SREEN_WIDTH-40:
        canvas.move(player,10,0)
    elif event.keysym == "Up" and canvas.coords(player)[0]>0:
        canvas.move(player,0,-10)
    elif event.keysym == "Down"and canvas.coords(player)[0]<SCREEN_HEIGHT:
        canvas.move(player,0,10)
    print(canvas.coords(player))


root.bind("<Key>", move)
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()