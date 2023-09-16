"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

#Immport the required libraries
from turtle import *
from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#Circle function, named differently since Turtle already includes a circle() function
def mod_circle(start, end):
    """Draw circle using two points as the diameter."""
    center = (start + end) / 2 #The is calculated to ensure the middle of the circle is drawn between the 2 points
    radius = abs(end - start) / 2 #This is calculated to move the pen to the bottom edge of a vertical diamter
    begin_fill()
    
    up()
    goto(center.x, center.y - radius) #The pen is placed on the bottom edge of the diameter
    down()
    circle(radius) #Draws the circle 
    
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y) #The pen is placed on the first chosen point
    down()
    begin_fill()
    
    #Loop that runs twice to draw the rectangle, by moving first on the x-axis and then on the y-axis
    for _ in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    side_length = abs(end - start) #The length of the triangle's sides is calculated (it's the same since it's equilateral)
    up()
    goto(start.x, start.y) #The pen is placed on the first chosen point
    down()
    begin_fill()
    
    #Loop that runs three times, draws the traingle side by side from the bottom left corner
    for _ in range(3):
        forward(side_length)
        left(120)
    
    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        if shape == circle:
            mod_circle(start, end)
        else:
            shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()