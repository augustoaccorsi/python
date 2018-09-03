import turtle
import math

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length/3) + 1
    step_lenth = arc_length/n
    step_angle = angle/n

    for i in range(n):
        t.fd(step_lenth)
        t.lt(step_angle)


t = turtle.Turtle()
arc(t,40,180)
turtle.mainloop()
