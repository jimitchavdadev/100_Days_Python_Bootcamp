import pygame
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Initialize pygame mixer for sound
pygame.mixer.init()

# Load sound files
bounce_sound = pygame.mixer.Sound("bounce.wav")
score_sound = pygame.mixer.Sound("game.wav")

# Function to play sound
def play_sound(sound):
    sound.play()

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Display instructions
instructions = Turtle()
instructions.color("white")
instructions.penup()
instructions.hideturtle()
instructions.write("Player 1: W/S | Player 2: Up/Down\nFirst to 10 points wins!", 
                   align="center", font=("Courier", 18, "normal"))
time.sleep(3)
instructions.clear()

# Listen to keyboard inputs
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Game loop
game_is_on = True
winning_score = 10

while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        play_sound(bounce_sound)  # Wall collision sound

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        play_sound(bounce_sound)  # Paddle collision sound

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        play_sound(score_sound)  # Scoring sound

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        play_sound(score_sound)  # Scoring sound

    # Check for game over
    if scoreboard.l_score == winning_score or scoreboard.r_score == winning_score:
        game_is_on = False

# Display Game Over screen
game_over = Turtle()
game_over.color("white")
game_over.penup()
game_over.hideturtle()
winner = "Left Player" if scoreboard.l_score == winning_score else "Right Player"
game_over.write(f"Game Over! {winner} Wins!", align="center", font=("Courier", 24, "normal"))

screen.exitonclick()
