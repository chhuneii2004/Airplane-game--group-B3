import tkinter as tk
from PIL import Image, ImageTk
import random
import winsound

SCREEN_WIDTH = 600
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
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
root.title("Skyfall")

canvas = tk.Canvas(root)
canvas.pack()

# Insert background image
bg_image = Image.open("images/starbackground.png")
bg_image = ImageTk.PhotoImage(bg_image)
canvas.create_image(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, image=bg_image)

# Create player
player_img = Image.open("images/f15.png")
player_img = player_img.resize((PLAYER_WIDTH, PLAYER_HEIGHT))
player_img = ImageTk.PhotoImage(player_img)
player = canvas.create_image(SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_HEIGHT // 2, image=player_img)

# Create bullet image
bullet_img = Image.open("images/missile.png")
bullet_img = bullet_img.resize((BULLET_WIDTH, BULLET_HEIGHT))
bullet_img = ImageTk.PhotoImage(bullet_img)

# Create enemy image
enemy_img = Image.open("images/enemy.png")
enemy_img = enemy_img.resize((ENEMY_WIDTH, ENEMY_HEIGHT))
enemy_img = ImageTk.PhotoImage(enemy_img)

# Create the score label
score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack()

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()