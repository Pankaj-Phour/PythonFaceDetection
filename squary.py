import turtle

screen = turtle.Screen()
screen.setup(1920,1080)
square = turtle.Turtle()
square.speed(10)
square.hideturtle()


rectangle = turtle.Turtle()
rectangle.speed(10)
# rectangle.width(3)

rectangle.hideturtle()

circle = turtle.Turtle()
radius = 0
# circle.width(3)
circle.hideturtle()
circle.speed(10)

# clear = turtle.Turtle()
# clear.speed(10)
# clear.width(3)
# clear.hideturtle()
# clear._delay(10)
# clear2 = turtle.Turtle()
# clear2.width(3)
# clear2.speed(10)
# clear2.hideturtle()
# clear2._delay(10)

for i in range(300):
    if(i<50):
        color = 'green'
        color2 = 'blue'
    elif(i<100):
        color = 'aqua'
        color2 = 'orange'
    elif(i<150):
        color = 'orange'
        color2 = 'purple'
    elif(i<200):
        color = 'purple'
        color2 = 'red'
    elif(i<250):
        color = 'red'
        color2 = 'blue'
    else:
        color = 'blue'
        color2 = 'green'
    color3 = 'orange'
    # square.color(color)
    rectangle.color(color)
    # square.forward(i)
    rectangle.forward(i)
    rectangle.right(90)
    # square.left(360)
    circle.color(color3)
    circle.circle((radius + i)/2,45)
    

# for i in range(300):
#     color = 'white'
#     clear.color(color)
#     clear.left(40)
#     clear.forward(i)
#     clear2.color(color)
#     clear2.right(40)
#     clear2.forward(i)