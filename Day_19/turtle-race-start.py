from turtle import Turtle, Screen
from random import randint

# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []

# Create turtles and position them
for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])  # Corrected color assignment
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Start race only if user makes a valid bet
if user_bet and user_bet in colors:
    is_race_on = True
else:
    is_race_on = False
    print("Invalid bet. Please restart and enter a valid color!")

# Run the race
while is_race_on:
    for turtle in all_turtles:
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
        
        # Check if any turtle crosses the finish line
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")
            is_race_on = False

screen.exitonclick()
