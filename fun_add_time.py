import time
from datetime import datetime
import fun_add_num

now = datetime.now()

def Time(value, count):
    numbers = fun_add_num.numbers
    if value == 'H':
        return numbers[datetime.now().strftime("%H")[count]]
    if value == 'M':
        return numbers[datetime.now().strftime("%M")[count]]
    if value == 'S':
        return numbers[datetime.now().strftime("%S")[count]]

def Time_sleep():
    return time.sleep(0.3)