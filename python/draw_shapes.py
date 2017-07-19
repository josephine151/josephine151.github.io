from turtle import *
import math

#Josephine
Lina = Turtle()

# Set Up your screen and starting position.

setup(500,500)
x_pos = 0
y_pos = 0
Lina.setposition(x_pos, y_pos)

## without the penup() command, a it would be a square with a continous line as a side:
distance=(250)
pencolor("red")
fillcolor("blue")

for x in range(4):
    forward(distance)
    right(90)

penup()



# Close window on click.
exitonclick()
