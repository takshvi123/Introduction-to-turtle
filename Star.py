import turtle

b=turtle.Screen()
b.bgcolor("lavender")

b.setup(978,879)

t=turtle.Turtle()
t.pensize(18)
t.pencolor("pink")
t.penup()
t.goto(-60,0)
t.pendown()



for i in range (3):
  t.forward(200)
  t.left(120)
t.left(90)
t.penup()

t.forward(100)
t.pendown()
t.right(90)
for i in range (3):
  t.forward(200)
  t.right(120)

turtle.done()