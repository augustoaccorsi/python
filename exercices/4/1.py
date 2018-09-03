import turtle
import math

def polygon(tt, size, length):
    angle = 360/size
    total = 0.0
    for i in range(size):
            tt.fd(length)
            tt.lt(angle)
            total = total + angle
            print("step:",i,"size:",size, "angle:",total)

def circle(tt, radius):
    circumference = 2*math.pi*radius
    n = 50
    length = circumference/n
    polygon(tt,n,length)


tt = turtle.Turtle()
circle(tt, 100)
turtle.mainloop()
