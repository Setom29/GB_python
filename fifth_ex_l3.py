Sum = 0
flag = False


def isdigit_test_func(num):
    """Осуществляет проверку на то,
    можно ли переданную строку преобразовать в число
    и проверяет на наличие спец.символов.

    Позиционные аргументы:
    num -- переданная строка

    """
    if item.replace('.', '', 1).isdigit():
        return True
    elif num[0] == '-' and num[1:].replace('.', '', 1).isdigit():
        return True
    else:
        return False


while True:
    calc_list = input('Введите строку: ').split()
    for item in calc_list:
        if isdigit_test_func(item):
            Sum += float(item)
            print('i am here')
        else:
            flag = True
            break
    print(Sum)
    if flag:
        break
