# from turtle import Turtle, Screen

# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.penup()
# timmy.speed(1)
# timmy.forward(100)

# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table =PrettyTable()
table.add_column("Pokemon Name",["pikachu", "squirtle", "charmender"])
table.add_column("type",["electric", "water",""])
table.align="c"

print(table)