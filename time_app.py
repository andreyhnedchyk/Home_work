import os
import time

import fun_add_num
import fun_add_time


clear = lambda: os.system('cls')


cube = '\u2B1B'
list_color = [31, 31, 33, 33, 35, 35, 36, 36]
Time = fun_add_time.set_time
point = fun_add_num.points
counter = 0
tire = 0


while True:
    for color in range(8):
        if tire == 7 or counter == 1:
            counter = 1
            tire -= 1

        for i in range(8):
            print(' ', *Time('H', 0)[i], ' ' * 4, *Time('H', 1)[i], ' ' * 3, point(tire, i), ' ' * 2, *Time('M', 0)[i], ' ' * 4, *Time('M', 1)[i], ' ' * 3, point(tire, i), ' ' * 2, *Time('S', 0)[i], ' ' * 4, *Time('S', 1)[i])
        print(f"\033[{list_color[color]}m{cube}")

        if counter == 0 or tire == 0:
            counter = 0
            tire += 1

        time.sleep(0.3)
        clear()
        print()

