# -----------------------------------------+
# Lukas Bernard                            |
# CSCI 127, In Lab 1                       |
# -----------------------------------------|
# Modify an etch-a-sketch program.         |
# -----------------------------------------+

import turtle
import random
v=1

window = turtle.Screen()

pencil = turtle.Turtle()
square = turtle.Turtle()

# ---------------------------------

def draw_square(square, v):  
    square.up()
    square.goto(-200, 200)
    square.down()
    red = random.random()
    green = random.random()
    blue = random.random()
    if(v != 1):
        square.begin_fill()
        for i in range(4):
            square.forward(50)
            square.right(90)
            square.color(red, green, blue)
        square.end_fill()
    if(v == 1):
        square.begin_fill()
        for i in range(4):
            square.forward(50)
            square.right(90)
        square.end_fill()
        v+1
    return red, green, blue

# ---------------------------------

def drawing_controls(x, y):
    if (-200 <= x <= -150) and (150 <= y <= 200):
        draw_square(square, v)
        pencil.color(red, green, blue)


# ---------------------------------

def main():
    pencil.shape("circle")

    text = turtle.Turtle()
    text.hideturtle()
    text.up()
    text.goto(-205, 205)
    text.write("Change Color")

    square.speed(0)
    square.hideturtle()
    draw_square(square, v)

    window.onclick(drawing_controls)
    pencil.onrelease(pencil.goto)

# ---------------------------------

main()
