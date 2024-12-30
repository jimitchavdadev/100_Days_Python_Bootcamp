from turtle import Turtle, Screen
from random import choice, random

timmy=Turtle()
timmy.shape("turtle")
timmy.color("red")


# square
# for i in range(100)
# timmy.forward(100)
# timmy.setheading(270)
# timmy.forward(100)
# timmy.setheading(180)
# timmy.forward(100)
# timmy.setheading(90)
# timmy.forward(100)

# dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# polygons
# sides=10

# for side in range(3,sides+1,1):
#     angle=360/side
#     for i in range(side):
#         timmy.forward(100)
#         timmy.left(angle)    

# random walk
def random_color():
    red = random()  
    green =random()
    blue = random() 
    return (red, green, blue)

# dirs=[0,90,180,270]
# steps=10
# timmy.pensize(10)
# for i in range(steps+1):
#     timmy.setheading(choice(dirs))
#     timmy.color(random_color())
#     timmy.forward(100)

# spirograph
# timmy.speed("fastest")
# times=50
# def spirograph(size):
#     shift=360/size
#     for i in range(times+1):
#         timmy.color(random_color())
#         timmy.circle(100)
#         curr=timmy.heading()
#         timmy.setheading(curr+shift)
# spirograph(times)

screen=Screen()
screen.exitonclick()