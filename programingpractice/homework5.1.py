import turtle


t = turtle.Turtle()
s = turtle.Screen()

t.hideturtle()
t.speed(0)
s.tracer(0)

#横線
t.penup()
t.setpos(-400,400)
t.pendown()
for i in range(0,100):
    t.forward(800)
    t.penup()
    t.setpos(-400,400-(20*i))
    t.pendown()


#縦線
t.penup()
t.setpos(-400,400)
t.pendown()
t.right(90)
for i in range(0,100):
    t.forward(800)
    t.penup()
    t.setpos(-400+(20*i),400)
    t.pendown()

turtle.done()
