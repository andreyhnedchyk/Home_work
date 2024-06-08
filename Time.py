from datetime import datetime


now = datetime.now()


hours_string = now.strftime("%H")


cube = '\u2B1B'

one = [
    [cube * 8],
    [cube * 8],
    [12 * ' ', cube*2],
    [12 * ' ', cube*2],
    [12 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    ]

zero = [
    [cube * 8],
    [cube * 8],
    [cube * 3, 2 * ' ', cube * 3],
    [cube * 3, 2 * ' ', cube * 3],
    [cube * 3, 2 * ' ', cube * 3],
    [cube * 3, 2 * ' ', cube * 3],
    [cube * 8],
    [cube * 8],
    ]

six = [
    [cube * 8],
    [cube * 2],
    [cube * 8],
    [cube * 8],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 8],
    [cube * 8],
    ]

two = [
    [4 * ' ', cube * 4, 4 * ' '],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [10 * ' ', cube],
    [4 * ' ', cube * 2, 4 * ' '],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 8],
    [cube * 8],
    ]

tree = [
    [cube * 8],
    [cube * 2, 7 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    [5 * ' ', cube * 5],
    [5 * ' ', cube * 5],
    [12 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 8],
    ]

eight = [
    [cube * 8],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [8 * ' ', cube * 2],
    [3 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 8],
    ]
for i in range(8):
    print(*one[i], (' ' * 3), *eight[i])