###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
from turtle import Turtle, Screen
from random import choice

# List of RGB colors
rgb_colors = [(245, 243, 238), (247, 242, 244), (240, 245, 241), (202, 164, 109), 
              (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), 
              (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), 
              (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), 
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), 
              (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), 
              (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), 
              (174, 94, 97), (176, 192, 209)]

# Initialize turtle and screen
timmy = Turtle()
screen = Screen()
screen.colormode(255)  # Set color mode to accept 0-255 RGB values
timmy.speed("fastest")  # Speed up the turtle
timmy.penup()

# Move to starting position
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

# Number of dots
num_dots = 100

# Draw the dots
for dot_count in range(1, num_dots + 1):
    timmy.dot(20, choice(rgb_colors))
    timmy.forward(50)

    if dot_count % 10 == 0:  # Move to the next row
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

# Exit on click
screen.exitonclick()
