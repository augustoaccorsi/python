import turtle

def square(tt, len):
    for i in range(4):
            tt.fd(len)
            tt.lt(90)

tt = turtle.Turtle()

square(tt, 300)
turtle.mainloop()
