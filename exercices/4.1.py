import turtle

def square(tt):
    for i in range(4):
            tt.fd(100)
            tt.lt(90)

tt = turtle.Turtle()

square(tt)
turtle.mainloop()
