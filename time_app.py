import os, time
import fun_add_time
import fun_add_num
clear = lambda: os.system('cls')

cube = '\u2B1B'
Time = fun_add_time.Time
point = fun_add_num.points
counter = 0
tire = 0
while True:
    if tire == 7 or counter == 1:
        counter = 1
        tire -= 1
    for i in range(8):
        print(*Time('H', 0)[i], ' ' * 4, *Time('H', 1)[i], ' ' * 3, point(tire, i), ' ' * 2, *Time('M', 0)[i], ' ' * 4, *Time('M', 1)[i], ' ' * 3, point(tire, i), ' ' * 2, *Time('S', 0)[i], ' ' * 4, *Time('S', 1)[i])

    if counter == 0 or tire == 0:
        counter = 0
        tire += 1

    time.sleep(0.3)
    clear()
    print()
    print()