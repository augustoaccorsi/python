import turtle
import math

def flower(tt, size, length, leaf):
    angle = 360/size
    total = 0.0
    for i in range(leaf*2):
            tt.fd(length)
            tt.lt(angle)
            total = total + angle

tt = turtle.Turtle()
#flower(tt, 30, 20, 6)

tt.fd(50)
tt.lt(54)
tt.fd(50)
tt.lt(54)

turtle.mainloop()
