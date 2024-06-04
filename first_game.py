import random
import os
import time

clear = lambda: os.system('cls')

print('Приветствую тебя! Добро пожаловать на игру "Кто хочет стать миллионером"')
input("Желаешь начать (нажми на любую кнопку :> )")
clear ()

print('Во время игры ты можешь воспользоваться помощью в виде двух подсказок')
time.sleep(2)
print('Звонок другу и 50/50')
time.sleep(1)
print('Во время игры нажми "1" или "2" в зависимости от выбранной подсказки ')
time.sleep(2)
print('Удачи )')
time.sleep(2)
clear()

true_answer = ''
count_question = 0
bank = 0
lose_case = ["Увы, это неверный ответ!" ,"Нет, к сожалению, не угадали.", "На этот раз фортуна не на вашей стороне.", "Не отчаивайтесь, еще много вопросов впереди!", "Ой, неправильный ответ, но это не конец игры!"]
def way(option):

    if option == 'question':
        print(global_questions[0].get('question'))
        print('...')
        print('Варианты ответов:')

    else:
        for i in global_questions[0].get('answers'):
            print(i[0])
        print('1. Звонок другу 2. 50/50')


def helper(choice):

    if choice == '2':
        return true_answer

    else:
        friend_luck = random.randint(0, 1)
        if friend_luck == 1:
            return true_answer
        else:
            return global_questions[0].get('answers')[2][0]


def game_answ(answ):
    global bank
    check_win = 0

    if answ == '2':
        print('Верно одно из двух ----', helper(answ), 'или', global_questions[0].get('answers')[3][0])
        answ = input('Окончательный ответ==> ')

    if answ == '1':
        print('Вы звоните другу ...')
        time.sleep(1)
        print('Он поднимает трубку')
        time.sleep(1)
        print('Хммм. Я думаю, что ответ может звучать так --->', helper(answ))
        time.sleep(1)
        answ = input('Окончательный ответ==> ')

    if answ == true_answer:
        print('Правильно')
        summ = 100 * count_question
        bank += summ
        print(f'Вы выйграли {summ} р.')
        check_win = 1
        time.sleep(1)
        clear()

    if check_win == 0:
        print(lose_case[0])
        time.sleep(2)
        clear()


global_questions = [
    {'question': 'Какой газ является основным компонентом атмосферы Земли?', 'answers': [['Азот', True], ['Кислород', False], ['Аргон', False], ['Углекислый газ', False]]},
    {'question': 'Какое животное является самым быстрым на Земле?', 'answers': [['Гепард', True], ['Лев', False], ['Тигр', False], ['Белорусский заяц', False]]},
    {'question': 'Сколько планет входит в Солнечную систему?', 'answers': [['8 планет', True], ['9 планет', False], ['10 планет', False], ['1 планета', False]]},
    {'question': 'Как называется ядерная реакция протекающая в Солнце?', 'answers': [['Термоядерный синтез', True], ['Атомный распад', False], ['Водородное расщепление', False], ['Инфляция в Беларуси', False]]},
    {'question': 'Какое самое крупное животное на Земле?', 'answers': [['Голубой кит', True], ['Африканский страус', False], ['Гребнистый крокодил', False], ['Зеленая анаконда', False]]},
    {'question': 'Какой океан самый большой по площади?', 'answers': [['Тихий океан', True], ['Атлантический океан', False], ['Индийский океан', False], ['Северный Ледовитый океан', False]]},
    {'question': 'Какой металл является самым легким?', 'answers': [['Литий', True], ['Алюминий', False], ['Железо', False], ['Ртуть', False]]},
    {'question': 'Как называется вторая по величине планета в Солнечной системе?', 'answers': [['Сатурн', True], ['Уран', False], ['Меркурий', False], ['Венера', False]]},
    {'question': 'Сколько месяцев в году имеет високосный год?', 'answers': [['12 месяцев', True], ['11 месяцев', False], ['10 месяцев', False], ['13 месяцев', False]]},
    {'question': 'Как называется процесс движения планет по орбите вокруг Солнца? ', 'answers': [['Обращение', True], ['Круговращение', False], ['Обход', False], ['Полет', False]]},
]


while len(global_questions) != 0:
    count_question += 1
    random.shuffle(global_questions), random.shuffle(lose_case)
    true_answer = global_questions[0].get('answers')[0][0]
    random.shuffle(global_questions[0].get('answers'))
    way('question')
    way('answers')
    game_answ(input('Ваш ответ ==>'))
    global_questions.pop(0)
    if len(global_questions) == 0:
        print(f'Игра окончена. Вы выйграли {bank} р.')
# проверка