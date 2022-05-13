"""
Ejercicios:
1. Número de taps
2. Detectar cuando todos los cuadros se han destapado
3. Centrar el dígito en el cuadro
4. Innovación
"""
#Libraries are imported
from itertools import count
from random import *
from tkinter import CENTER
from turtle import *
from freegames import path

#Global variables are defined
car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
count = 0
uncoveredImages = 0

#Square function creates a square taking two parameters x and y as dimensions.
def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global count
    global uncoveredImages

    spot = index(x, y)
    mark = state['mark']
    count += 1
    print("Taps:", count)

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        uncoveredImages += 1
    
    if(uncoveredImages == 32):
        print('Congrats! You solved the puzzle')


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 27, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align=CENTER)

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()