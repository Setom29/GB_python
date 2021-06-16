class NotNumException(Exception):
    def __init__(self, txt):
        self.text = txt


def is_valid(is_num):  # проверяет коррректность числа, не примет 0123 123. 12-3 и т.д.
    if is_num.count('-') == 1:
        if is_num[0] == '-':
            is_num = is_num.replace('-', '')
        else:
            return False
    if is_num.count('.') == 1 and is_num[0] != '.' and is_num[-1] != '.':
        is_num = is_num.split('.')
        if len(is_num) == 2:
            for el in is_num[1]:
                if el.isdigit():
                    continue
                else:
                    return False
        for el in is_num[0]:
            if el.isdigit():
                continue
            else:
                return False
        if len(str(int(is_num[0]))) == len(is_num[0]):  # Проверяет наличие нуля. Случаи: 0123.4
            return True
        else:
            return False
    elif is_num.count('.') == 0:
        for el in is_num:
            if el.isdigit():
                continue
            else:
                return False
        if len(str(int(is_num))) == len(is_num):  # Проверяет наличие нуля. Случаи: 0123
            return True
        else:
            return False
    else:
        return False


lst = []
while True:
    try:
        temp = input('Write a number or press Enter to exit: ').strip().lower()
        if temp == '':
            print(*lst)
            break
        elif is_valid(temp):
            lst.append(temp)
        else:
            raise NotNumException('Not a number.')
    except NotNumException as err:
        print(err)
