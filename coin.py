def admin_check(func):
    def wrapper(user_name):
        if username == 'admin':
            return func(username)
        else:
            return 'Доступ запрещен'
    return wrapper

@admin_check
def get_account_balance(user_name):
    return f'Сумма на счете: 300 р'

username = input('Введите логин: ')

result = get_account_balance(username)

print(result)