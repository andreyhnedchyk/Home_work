import time
from datetime import datetime
import os

clear = lambda: os.system('cls')
now = datetime.now()

cube = '\u2B1B'

numbers = {
    '1' : [
    [10 * ' ',cube * 3],
    [8 * ' ',cube * 4],
    [12 * ' ', cube*2],
    [12 * ' ', cube*2],
    [12 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    ],
    '2' : [
    [4 * ' ', cube * 4, 3 * ' '],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [10 * ' ', cube, 3 * ' '],
    [4 * ' ', cube * 2, 7 * ' '],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 8],
    [cube * 8],
    ],
    '3' : [
    [cube * 8],
    [cube * 2, 7 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    [5 * ' ', cube * 5],
    [5 * ' ', cube * 5],
    [12 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 8],
    ],
    '4' : [
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube*2],
    [cube*8],
    [cube*8],
    [ (cube * 2).rjust(15)],
    [12 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    ],
    '5' : [
    [cube * 8],
    [cube * 8],
    [cube * 2, 12 * ' '],
    [cube * 8],
    [12 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    [cube * 8],
    [cube * 8]
    ],
    '6' : [
    [cube * 8],
    [cube * 2, 12 * ' '],
    [cube * 8],
    [cube * 8],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 8],
    [cube * 8],
    ],
    '7' : [
    [cube * 8],
    [cube * 8],
    [12 * ' ', cube*2],
    [10 * ' ', cube*2, 2 * ' '],
    [8 * ' ', cube * 2, 4 * ' '],
    [6 * ' ', cube * 2, 6 * ' '],
    [4 * ' ', cube * 2, 8 * ' '],
    [2 * ' ', cube * 2, 10 * ' '],
    ],
    '8' : [
    [cube * 8],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [8 * ' ', cube * 2],
    [3 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 8],
    ],
    '9' : [
    [cube * 8],
    [cube * 8],
    [cube * 3, 2 * ' ', cube * 3],
    [cube * 8],
    [cube * 8],
    [8 * ' ', cube * 3],
    [cube * 8],
    [cube * 8],
    ],
    '0' : [
    [cube * 8],
    [cube * 8],
    [cube * 3, 2 * ' ', cube * 3],
    [cube * 3, 2 * ' ', cube * 3],
    [cube * 3, 2 * ' ', cube * 3],
    [cube * 3, 2 * ' ', cube * 3],
    [cube * 8],
    [cube * 8],
    ],
}

def Time(value, count):
    if value == 'H':
        return numbers[datetime.now().strftime("%H")[count]]
    if value == 'M':
        return numbers[datetime.now().strftime("%M")[count]]
    if value == 'S':
        return numbers[datetime.now().strftime("%S")[count]]

# for i in range(8):
#     print(*numbers['0'][i],' ' * 3,*numbers['4'][i])

while True:
    for i in range(8):
        print(*Time('H', 0)[i], ' ' * 4, *Time('H', 1)[i], ' ' * 6, *Time('M', 0)[i], ' ' * 4, *Time('M', 1)[i], ' ' * 6, *Time('S', 0)[i], ' ' * 4, *Time('S', 1)[i])
    time.sleep(1)
    clear()
    print()
    print()