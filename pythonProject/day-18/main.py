from turtle import Turtle, Screen

tim = Turtle()
# tim.shape("turtle")
# tim.color("red")

# for _ in range(4):
#     tim.forward(10)
#     tim.penup(10)
#     # tim.right(90)


def draw_shapes(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    draw_shapes(shape_side_n)


screen = Screen()
screen.exitonclick()