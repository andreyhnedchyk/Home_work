import datetime
import os
import fun_add_num

clear = lambda: os.system('cls')

cube = '\u2B1B'
numbers = fun_add_num.numbers

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