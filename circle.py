import turtle
myTurtle = turtle.Turtle()
myTurtle.ht()
myTurtle.pensize(10)
myTurtle.speed(100)
while True:
    for count in range(36):
        myTurtle.pencolor("black")
        myTurtle.shape("circle")
        myTurtle.forward(10)
        myTurtle.right(10)
    for count in range(36):
        myTurtle.pencolor("white")
        myTurtle.forward(10)
        myTurtle.right(10)
