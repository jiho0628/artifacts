import turtle

from math import cos,sin, pi

PI=pi


t = turtle.Turtle()

def draw_my_heart(ttl, x, y, radius, alpha=45, theta=210, degrees=0):
    ttl.setheading(degrees)
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()


    r = radius # 扇形の半径
    a = alpha # 水平方向と直線の角度
    t = theta # 扇形の中心角

  
    straight = r*(-cos((a+90)*PI/180)-cos((t+a-90)*PI/180)) / cos(a*PI/180)

    ttl.left(a)
    ttl.forward(straight)
    ttl.circle(r,t)
    ttl.left(720-2*a-2*t)
    ttl.circle(r,t)
    ttl.forward(straight)

width=700 
height=700 
x = 0
y = -150
r = 100

draw_my_heart(t, x, y, r)

turtle.done()
