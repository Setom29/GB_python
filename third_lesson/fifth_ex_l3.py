Sum = 0
flag = False
special_symbol = '$'  # спец. символ


def is_num_test_func(num):
    """Осуществляет проверку на то,
    можно ли переданную строку преобразовать в число
    и проверяет на наличие спец.символов.

    Позиционные аргументы:
    num -- переданная строка

    """
    try:
        num = float(num)
        return 1
    except ValueError:
        if num == special_symbol:
            return 0
        else:
            return -1


print(f'Спец. символ: {special_symbol}')
while True:
    calc_list = input('Введите строку: ').split()
    temp = 0
    for item in calc_list:
        if is_num_test_func(item) == 1:
            temp += float(item)
        elif is_num_test_func(item) == 0:
            print('Введен спец. символ!')
            flag = True
            break
        elif is_num_test_func(item) == -1:
            print(f'Ошибка ввода: "{item}"')
            continue
    Sum += temp
    print(f'{Sum}({temp})')
    if flag:
        break
