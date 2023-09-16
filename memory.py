"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
#tiles = list(range(32)) * 2

letters = [chr(i) for i in range(65, 65 + 32)] # Generates numbers for ASCII characters from 65 to 97, and converts them to letters
tiles = letters * 2 # Doubles the list "letters" to create pairs of characters, instead of using numbers

state = {'mark': None}
hide = [True] * 64
taps = 0  # Initialize counter for taps

# Function to count the taps
def count_taps():
    global taps
    taps += 1

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
    spot = index(x, y)
    mark = state['mark']
    count_taps()  # Call the tap counting function at each tap

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

# Function to display the tap count
def show_taps():
    up()
    goto(-200, 180)
    color('black')
    write(f'Taps: {taps}', font=('Arial', 16, 'normal'))

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    hidden_tiles = sum(1 for tile in hide if tile)  # Count the hidden tiles, it helps detect when all tiles are revealed

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 8, y + 9) # Adjust the position of the number to be more centered on the tile
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    show_taps()  # Call the function to show the tap count

    update()

    # Check if all tiles are revealed, and if they are display a message of acknolwedgement
    if hidden_tiles == 0:
        up()
        goto(-150, -20)
        color('black')
        write("Congratulations!", font=('Arial', 40, 'bold'))

    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()