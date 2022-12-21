import turtle

def draw_square(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)

def main():
    drawing = turtle.Screen()
    drawing.bgcolor("white")

    alex = turtle.Turtle()
    alex.shape("turtle")
    alex.pensize(10)
    alex.color("blue")

    for i in range(60):
        draw_square(alex, 150)
        alex.left(5)

    drawing.exitonclick()

main()