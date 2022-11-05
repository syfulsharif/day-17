from prettytable import PrettyTable
from turtle import Turtle, Screen

timmy = Turtle()
table = PrettyTable()
print(timmy)
timmy.shape("turtle")
timmy.color('coral')
timmy.forward(100)
my_screen = Screen()
my_screen.exitonclick()

table.add_column("Employee_Name", ["Alexandar", "Nick", "Rossy"])
table.add_column("Salary", [2000, 3000, 5000])
print(table)