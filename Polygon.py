import turtle
b=turtle.Screen()
b.bgcolor("lavender")
b.setup(978,879)

t=turtle.Turtle()
t.pensize(8)
t.pencolor("lightpink")
for i in range (6):
    t.forward(111)
    t.right(90)
    t.forward(199)
    t.right(90)
turtle.done()