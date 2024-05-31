data = 'Не знаю, как там в Лондоне, я не была. Может, там собака друг человека. А у нас управдом друг человека!'
print('Шаг 1 - Количество символов -', len(data))
print('Шаг 2 - Развернутая строка -',data[::-1])
print('Шаг 3 - Слова с большой буквы -',data.title())
print('Шаг 4 - Текст с прописными буквами -',data.upper())

one, two, tree = data.count('нд'), data.count('ам'), data.count('о')
print(f'Шаг 5 - Количесво вхождений "нд" = {one}, количесво вхождений "ам" = {two}, количесво вхождений "о" = {tree}')
print('Шаг 6 - Текст с удаленными пробелами -',data.replace(' ', ''))
print('Шаг 7 - Поиск по индексу слова "Может" - ',data.index("Может"))

rule = data.split()
print('Шаг 8 - Развернутое предложение -', *rule[::-1])
print('Шаг 9 - Исходная строка -', data)