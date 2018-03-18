import turtle
turtle.setup(800, 600)

# set coordinates of the wall
left = -300
right = 300
top = 200

turtle1 = turtle.Turtle()
turtle1.hideturtle()

# draw a horizontal wall
turtle1.penup()
turtle1.setposition(left, top)
turtle1.pendown()
turtle1.setposition(right, top)

# create a turtle
turtle2 = turtle.Turtle()
turtle2.shape('turtle')
turtle2.penup()
turtle2.left(90)

# walk upward, turn around when hitting the wall
for i in range(400):
    turtle2.forward(1)
    if turtle2.ycor() >= top:
        turtle2.left(180)

turtle.exitonclick()