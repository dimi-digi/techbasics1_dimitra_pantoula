import turtle
import random
from turtle import *

# --- Initial Setup ---
width = 600
height = 600
setup(width, height)
tracer(0, 0)
bgcolor('#0a192f')


palette = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]
moon_colors = ["#f0f8ff", "#e6e6fa", "#fffaf0"]
sea_colors = ["#1d3557", "#457b9d", "#a8dadc"]


penup()
goto(10, 100)
pendown()

for i in range(36):

    fillcolor(random.choice(moon_colors))
    begin_fill()
    circle(80)
    end_fill()
    right(10)


color("black")
for i in range(12):
    # Nested loop for the triangle
    for side in range(3):
        forward(50)
        left(120)
    right(30)


# We use randomness to make the lines look like light reflecting on waves
for i in range(60):
    # Randomly pick a color and a position for each "wave"
    line_color = random.choice(sea_colors)
    line_length = random.randint(20, 150)

    # Position the lines in the bottom half of the screen
    x = random.randint(-250, 200)
    y = random.randint(-280, -20)

    penup()
    goto(x, y)
    pendown()

    color(line_color)
    forward(line_length)

# Final signature or detail
penup()
goto(-250, -260)


update()
done()