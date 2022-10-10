# Importing turtle 
# A tool used to design patterns and anything that can be drawn in python 
# With turtle we can design any shape or design 

import turtle

# setting screen size of python turtle grpahics screen to a variable named sc
sc = turtle.Screen()

# setting turtle to a variable named pen 
pen = turtle.Turtle()

def rainbow(color,circle,value):
    pen.color(color)
    pen.circle(circle,-180)
    pen.up()
    pen.setpos(value,0)
    pen.down()
    pen.right(90)

colors = ['violet','indigo','blue','green','yellow','orange','red','violet','indigo','blue','green','yellow','orange','red','violet','indigo','blue','green','yellow','orange','red','violet','indigo','blue','green','yellow','orange','red']

sc.setup(1920,1080)
sc.bgcolor('black')

pen.right(180)
pen.width(2)
pen.speed(10)
def draw():
    for i in range(28):
        rainbow(colors[i],5*(i+8),-5)


for i in range(1):
    draw()

pen.hideturtle()

