height, weight = input('Введите свой рост и вес в см через пробел ==>').split()
bmi = int(weight)/((int(height) / 100) ** 2)
print('Ваш индекс массы тела',bmi)
print('15' + ('=' * (int(bmi) - 15)) + '|' + ('=' * (25 - (int(bmi) - 15))) + '40')

