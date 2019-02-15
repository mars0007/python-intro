import turtle

def satan(size):
    for i in range(5):
        turtle.fd(size)
        turtle.lt(144)

#satan(200)

turtle.clear()

def polygon(size, sides):
    angle = 360/sides
    for i in range(sides):
        turtle.fd(size)
        turtle.lt(angle)

polygon(1,1000)
