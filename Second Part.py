import turtle

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

window = turtle.Screen()
window.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.width(3)

radius = 10

for _ in range(720):
    pen.pencolor(colors[_ % len(colors)])
    pen.forward(radius)
    pen.left(59)
    radius += 1

pen.hideturtle()

turtle.done()
