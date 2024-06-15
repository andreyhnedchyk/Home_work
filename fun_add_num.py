cube = '\u2B1B'
numbers = {
    '1': [
    [10 * ' ',cube * 3],
    [8 * ' ',cube * 4],
    [12 * ' ', cube*2],
    [12 * ' ', cube*2],
    [12 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    ],
    '2': [
    [4 * ' ', cube * 4, 3 * ' '],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [10 * ' ', cube, 3 * ' '],
    [4 * ' ', cube * 2, 7 * ' '],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 8],
    [cube * 8],
    ],
    '3': [
    [cube * 8],
    [cube * 2, 7 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    [5 * ' ', cube * 5],
    [5 * ' ', cube * 5],
    [12 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 8],
    ],
    '4': [
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube*2],
    [cube*8],
    [cube*8],
    [ (cube * 2).rjust(15)],
    [12 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    ],
    '5': [
    [cube * 8],
    [cube * 8],
    [cube * 2, 12 * ' '],
    [cube * 8],
    [12 * ' ', cube * 2],
    [12 * ' ', cube * 2],
    [cube * 8],
    [cube * 8]
    ],
    '6': [
    [cube * 8],
    [cube * 2, 12 * ' '],
    [cube * 8],
    [cube * 8],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 8],
    [cube * 8],
    ],
    '7': [
    [cube * 8],
    [cube * 8],
    [12 * ' ', cube*2],
    [10 * ' ', cube*2, 2 * ' '],
    [8 * ' ', cube * 2, 4 * ' '],
    [6 * ' ', cube * 2, 6 * ' '],
    [4 * ' ', cube * 2, 8 * ' '],
    [2 * ' ', cube * 2, 10 * ' '],
    ],
    '8': [
    [cube * 8],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [8 * ' ', cube * 2],
    [3 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 2, 7 * ' ', cube * 2],
    [cube * 8],
    ],
    '9': [
    [cube * 8],
    [cube * 8],
    [cube * 3, 2 * ' ', cube * 3],
    [cube * 8],
    [cube * 8],
    [8 * ' ', cube * 3],
    [cube * 8],
    [cube * 8],
    ],
    '0': [
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
Point = 2
pol = 6
def points(i, q):
    global Point, pol
    if i == q or q == i + 1 and i <= 6:
        return cube
    elif (q == pol)and i >= 7:
        pol -= 1
        print(pol)
        return cube
    else:
        return ' '
