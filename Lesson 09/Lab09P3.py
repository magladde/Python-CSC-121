# Lesson 09 lab problem 3

import turtle
turtle.setup(800, 600)
turtle1 = turtle.Turtle()
turtle1.hideturtle()

# draw x
turtle1.penup()
turtle1.setposition(-250, 75)
turtle1.pendown()
turtle1.setposition(-150, -75)

turtle1.penup()
turtle1.setposition(-150, 75)
turtle1.pendown()
turtle1.setposition(-250, -75)

# draw y
turtle1.penup()
turtle1.setposition(-125, 75)
turtle1.pendown()
turtle1.setposition(-75, 0)
turtle1.setposition(-75, -75)
turtle1.penup()
turtle1.setposition(-75, 0)
turtle1.pendown()
turtle1.setposition(-25, 75)

# draw z
turtle1.penup()
turtle1.setposition(0, 75)
turtle1.pendown()
turtle1.setposition(100, 75)
turtle1.setposition(0, -75)
turtle1.setposition(100, -75)

turtle.exitonclick()