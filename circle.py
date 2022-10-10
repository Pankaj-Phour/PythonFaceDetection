import turtle

circle = turtle.Turtle()
circle2 = turtle.Turtle()

screen = turtle.Screen()

screen.setup(1920,1080)

circle.speed(0)
circle.pensize(2)
circle.hideturtle()

circle2.speed(0)
circle2.pensize(1)
circle2.hideturtle()
# while(True):
for i in range(20):
    for colors in ['violet','indigo','blue','green','yellow','orange','red']:
        circle.color(colors)
        circle2.color(colors)
        circle.circle(100)
        circle2.circle(50)
        circle2.left(5)
        circle.left(10)
            