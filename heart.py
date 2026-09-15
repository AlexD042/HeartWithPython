import turtle as t
from math import sin, cos, atan2, pi
from random import uniform

s = t.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.tracer(0)
p = t.Turtle()
p.hideturtle()
p.speed(0)

goto = p.goto
penup = p.penup
pendown = p.pendown
width = p.width
pencolor = p.pencolor


def heart(a, scale):
    x = 16 * (sin(a)**3) * scale
    y = (13*cos(a) - 5*cos(2*a) - 2*cos(3*a) - cos(4*a)) * scale
    return x, y


for i in range(20000):
    a = uniform(0, 2 * pi)
    sc = uniform(0.5, 15.5)
    x, y = heart(a, sc)

    ang = atan2(y, x) + uniform(-0.5, 0.5)
    length = uniform(4, 14)

    pencolor(1.0, uniform(0.25, 0.55), uniform(0.65, 0.85))
    width(uniform(0.5, 1.2))
    penup()
    goto(x, y)
    pendown()
    goto(x + length * cos(ang), y + length * sin(ang))

    if i % 150 == 0:
        s.update()

for i in range(3500):
    a = uniform(0, 2 * pi)
    x, y = heart(a, 16.0)

    ang = atan2(y, x) + uniform(-0.35, 0.35)
    length = uniform(10, 32)

    pencolor(1.0, uniform(0.45, 0.75), uniform(0.75, 0.95))
    width(uniform(0.4, 0.9))
    penup()
    goto(x + uniform(-2, 2), y + uniform(-2, 2))
    pendown()
    goto(x + length * cos(ang), y + length * sin(ang))

    if i % 150 == 0:
        s.update()

s.update()
t.done()
