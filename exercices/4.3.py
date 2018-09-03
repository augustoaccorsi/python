import turtle

def pulygon(tt, size, len):
    for i in range(size):
            tt.fd(len)
            tt.lt(360/size)

tt = turtle.Turtle()

pulygon(tt, 18, 80)
turtle.mainloop()
