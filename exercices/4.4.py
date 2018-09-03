import turtle
import math

def polygon(tt, size, length):
    for i in range(size):
            tt.fd(length)
            tt.lt(360/size)

def circle(tt, t, r):
    circumference = 2*math.pi*r
    n = 50
    length = circumference/n
    polygon(tt,n,length)


tt = turtle.Turtle()
circle(tt, 20, 100)
turtle.mainloop()


print(size)
