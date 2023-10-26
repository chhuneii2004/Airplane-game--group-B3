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

# Create start game screen
def start_game():
    start_label.destroy()
    start_button.destroy()
    root.bind("<Left>", move_player)
    root.bind("<Right>", move_player)
    root.bind("<Up>", move_player)
    root.bind("<Down>", move_player)
    root.bind("<space>", lambda event: create_bullet())
    create_multiple_enemies()


start_label = tk.Label(root, text="wellcome to skyfall game", font=("Arial", 20))
start_label.pack(pady=50)
start_button = tk.Button(root, text="Start", font=("Arial", 16), command=start_game)
start_button.pack()


def move_player(event):
    if event.keysym == "Left" and canvas.coords(player)[0] > PLAYER_WIDTH // 2:
        canvas.move(player, -PLAYER_SPEED, 0)
    elif event.keysym == "Right" and canvas.coords(player)[0] < SCREEN_WIDTH - PLAYER_WIDTH // 2:
        canvas.move(player, PLAYER_SPEED, 0)
    elif event.keysym == "Up" and canvas.coords(player)[1] > PLAYER_HEIGHT // 2:
        canvas.move(player, 0, -PLAYER_SPEED)
    elif event.keysym == "Down" and canvas.coords(player)[1] < SCREEN_HEIGHT - PLAYER_HEIGHT // 2:
        canvas.move(player, 0, PLAYER_SPEED)


def create_bullet():
    x = canvas.coords(player)[0]
    y = canvas.coords(player)[1]
    bullet = canvas.create_image(x, y - PLAYER_HEIGHT // 2, image=bullet_img, tags="bullet")
    move_bullet(bullet)
    shotSound()

def move_bullet(bullet):
    bullet_coords = canvas.coords(bullet)
    if bullet_coords[1] > -BULLET_HEIGHT:
        canvas.move(bullet, 0, -BULLET_SPEED)
        check_collision(bullet)  # Check collision with enemies
        root.after(10, move_bullet, bullet)
    else:
        canvas.delete(bullet)


def check_collision(bullet):
    bullet_coords = canvas.coords(bullet)
    enemies = canvas.find_withtag("enemy")
    for enemy in enemies:
        enemy_coords = canvas.coords(enemy)
        if (bullet_coords[0] > enemy_coords[0] - ENEMY_WIDTH // 2 and
                bullet_coords[0] < enemy_coords[0] + ENEMY_WIDTH // 2 and
                bullet_coords[1] > enemy_coords[1] - ENEMY_HEIGHT // 2 and
                bullet_coords[1] < enemy_coords[1] + ENEMY_HEIGHT // 2):
            canvas.delete(bullet)
            canvas.delete(enemy)
            update_score(1)  # Increase score by 1



def update_score(points):
    global score
    score += points
    score_label.config(text="Score: " + str(score))
    

def create_enemy():
    x = random.randint(ENEMY_WIDTH // 2, SCREEN_WIDTH - ENEMY_WIDTH // 2)
    enemy = canvas.create_image(x, ENEMY_HEIGHT // 2, image=enemy_img, tags="enemy")
    move_enemy(enemy)

def move_enemy(enemy):
    enemy_coords = canvas.coords(enemy)
    if enemy_coords[1] < SCREEN_HEIGHT + ENEMY_HEIGHT // 2:
        canvas.move(enemy, 0, ENEMY_SPEED)
        root.after(10, move_enemy, enemy)
    else:
        canvas.delete(enemy)

def create_multiple_enemies():
    for _ in range(1):  # Spawn 1 enemy
        create_enemy()
    root.after(2000, create_multiple_enemies)  # Create enemies every 2 seconds


def shotSound():
    winsound.PlaySound("sound/cat.wav", winsound.SND_ASYNC)

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()