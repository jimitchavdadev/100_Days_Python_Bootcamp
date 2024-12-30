import pygame
import random
import math

# Initialize the pygame
pygame.init()

# Game window dimensions
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders")

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Player spaceship
player_img = pygame.image.load('/home/rebel/Roger/Training/100_Days_with_Python/Day_95/player.png')  # Make sure you have this image or replace with a simple rectangle
player_x = width / 2 - 32
player_y = height - 50
player_x_change = 0

# Alien ship
alien_img = pygame.image.load('/home/rebel/Roger/Training/100_Days_with_Python/Day_95/aliens.png')  # Use your alien sprite or use a simple rectangle
alien_width = 64
alien_height = 64
aliens = []

# Bullet
bullet_img = pygame.image.load('/home/rebel/Roger/Training/100_Days_with_Python/Day_95/bullet.png')  # Use your bullet sprite or use a simple rectangle
bullet_width = 16
bullet_height = 32
bullet_x = 0
bullet_y = height - 50
bullet_y_change = 10
bullet_state = "ready"  # "ready" means the bullet is ready to be fired, "fire" means the bullet is moving

# Set up font
font = pygame.font.SysFont("arial", 32)
score = 0

# Game over text
game_over_font = pygame.font.SysFont("arial", 64)

# Create aliens
def create_aliens():
    for i in range(5):
        for j in range(5):
            alien = {
                "x": random.randint(50, 750),
                "y": random.randint(50, 150),
                "x_change": 4,
                "y_change": 40
            }
            aliens.append(alien)

def draw_aliens():
    for alien in aliens:
        screen.blit(alien_img, (alien["x"], alien["y"]))

def player(x, y):
    screen.blit(player_img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y))

def is_collision(alien_x, alien_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(alien_x - bullet_x, 2) + math.pow(alien_y - bullet_y, 2))
    if distance < 27:
        return True
    return False

def show_score(x, y):
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (x, y))

def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, red)
    screen.blit(game_over_text, (width / 2 - 200, height / 2))

create_aliens()

# Game loop
running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Player movement
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= width - 64:
        player_x = width - 64

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
        if bullet_y <= 0:
            bullet_y = height - 50
            bullet_state = "ready"

    # Alien movement
    for alien in aliens:
        alien["x"] += alien["x_change"]
        if alien["x"] <= 0 or alien["x"] >= width - alien_width:
            alien["x_change"] = -alien["x_change"]
            alien["y"] += alien["y_change"]

        if is_collision(alien["x"], alien["y"], bullet_x, bullet_y):
            score += 1
            bullet_y = height - 50
            bullet_state = "ready"
            alien["x"] = random.randint(50, 750)
            alien["y"] = random.randint(50, 150)

        if alien["y"] >= height - 64:
            game_over()
            break

    # Draw player, aliens, and score
    player(player_x, player_y)
    draw_aliens()
    show_score(10, 10)

    pygame.display.update()

pygame.quit()
