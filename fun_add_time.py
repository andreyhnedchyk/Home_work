import datetime
from datetime import datetime
import fun_add_num

cube = '\u2B1B'
now = datetime.now()

def set_time(value, count):
    numbers = fun_add_num.numbers
    if value == 'H':
        return numbers[datetime.now().strftime("%H")[count]]
    if value == 'M':
        return numbers[datetime.now().strftime("%M")[count]]
    if value == 'S':
        return numbers[datetime.now().strftime("%S")[count]]


