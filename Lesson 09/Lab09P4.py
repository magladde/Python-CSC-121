# Lesson 09 lab problem 4

import turtle
turtle.setup(800, 600)
turtle1 = turtle.Turtle()
turtle1.hideturtle()

# draw left wall
turtle1.penup()
turtle1.setposition(-300, 200)
turtle1.pendown()
turtle1.setposition(-300, -200)

# draw right wall
turtle1.penup()
turtle1.setposition(300, 200)
turtle1.pendown()
turtle1.setposition(300, -200)

# create turtle
turtle2 = turtle.Turtle()
turtle2.shape('turtle')
turtle2.penup()

# move turtle 2,000 pixels
for i in range(2000):
    turtle2.forward(1)
    if turtle2.xcor() == 300:
        turtle2.left(180)

    if turtle2.xcor() == -300:
        turtle2.left(180)

turtle.exitonclick()