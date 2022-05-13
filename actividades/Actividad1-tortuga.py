"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from math import hypot

import turtle

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.begin_fill()

    for count in range(4):
        turtle.forward(end.x - start.x)
        turtle.left(90)

    turtle.end_fill()


def newcircle(start, end):
    """Draw circle from start to end."""
    turtle.up()
    turtle.goto(start.x, (start.y + (start.y / 2)))
    radius = round(hypot((start.x - end.x),(start.y - end.y)), 1)
    turtle.begin_fill()
    turtle.circle(radius, 360)
    turtle.end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.begin_fill()

    for count in range(2):
        turtle.forward(end.x - start.x)
        turtle.left(90)
        turtle.forward(end.y - start.y)
        turtle.left(90)

    turtle.end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.begin_fill()

    for count in range(3):
        turtle.forward(end.x - start.x)
        turtle.left(120)

    turtle.end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value
    
def color(value):
    turtle.pencolor(value)
    turtle.fillcolor(value)

state = {'start': None, 'shape': line}
turtle.setup(420, 420, 370, 0)
turtle.onscreenclick(tap)
turtle.listen()
turtle.onkey(turtle.undo, 'u')
turtle.onkey(lambda: color('black'), 'k')
turtle.onkey(lambda: color('white'), 'w')
turtle.onkey(lambda: color('green'), 'g')
turtle.onkey(lambda: color('blue'), 'b')
turtle.onkey(lambda: color('red'), 'R')
turtle.onkey(lambda: store('shape', line), 'l')
turtle.onkey(lambda: store('shape', square), 's')
turtle.onkey(lambda: store('shape', newcircle), 'c')
turtle.onkey(lambda: store('shape', rectangle), 'r')
turtle.onkey(lambda: store('shape', triangle), 't')
turtle.done()
