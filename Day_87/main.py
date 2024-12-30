import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, -230)
ball.dx = 2
ball.dy = 2

# Bricks
brick_colors = ["red", "green", "blue", "yellow", "orange"]
bricks = []

for i in range(5):  # Create 5 rows of bricks
    for j in range(10):  # 10 bricks in each row
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(brick_colors[i % len(brick_colors)])
        brick.penup()
        brick.goto(-350 + (j * 70), 250 - (i * 30))  # Position bricks
        bricks.append(brick)

# Scoreboard
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions for moving the paddle
paddle_speed = 20

def move_left():
    x = paddle.xcor()
    if x > -350:
        x -= paddle_speed
    paddle.setx(x)

def move_right():
    x = paddle.xcor()
    if x < 350:
        x += paddle_speed
    paddle.setx(x)

# Keyboard bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Ball movement and collision logic
def update_score():
    score_display.clear()
    score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Main game loop
while True:
    screen.update()  # Manually update the screen to control the frame rate

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball collision with walls
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1  # Bounce the ball back

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1  # Bounce the ball back

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Bounce the ball back

    if ball.ycor() < -290:  # Ball falls off the screen (game over)
        ball.goto(0, -230)
        ball.dx = 2
        ball.dy = 2
        score = 0
        update_score()

    # Ball collision with paddle
    if (ball.ycor() > paddle.ycor() - 10 and
        ball.ycor() < paddle.ycor() + 10 and
        (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50)):
        ball.sety(paddle.ycor() + 10)
        ball.dy *= -1

    # Ball collision with bricks
    for brick in bricks:
        if (brick.xcor() - 30 < ball.xcor() < brick.xcor() + 30 and
            brick.ycor() - 15 < ball.ycor() < brick.ycor() + 15):
            brick.hideturtle()  # Hide the brick
            bricks.remove(brick)  # Remove the brick from the list
            ball.dy *= -1  # Ball bounces off the brick
            score += 10  # Increase score
            update_score()

    # Check if all bricks are destroyed (win condition)
    if len(bricks) == 0:
        ball.goto(0, -230)
        ball.dx = 0
        ball.dy = 0
        score_display.clear()
        score_display.write("You Win! Final Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        break  # Exit the game loop
