# Lesson 09 lab problem 1

import turtle
turtle.setup(800, 600)
turtle1 = turtle.Turtle() #creates turtle object
turtle1.hideturtle()

turtle1.penup()
turtle1.setposition(-200, 200)
turtle1.pendown()
turtle1.setposition(0, 200)

turtle1.penup()
turtle1.setposition(-200, 200)
turtle1.pendown()
turtle1.setposition(-200, -200)
turtle1.setposition(0, -200)

turtle1.penup()
turtle1.setposition(-200, 0)
turtle1.pendown()
turtle1.setposition(-75, 0)

turtle.exitonclick()