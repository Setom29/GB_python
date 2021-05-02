def zero_division(p_1, p_2):
    """Возвращает частное от деления.

    Позиционные аргументы:
    p_1 -- делимое
    p_2 --  делитель

    """

    if p_2 == 0:
        return ZeroDivisionError
    else:
        return p_1 / p_2


n_1 = float(input('Введите делимое: '))
n_2 = float(input('Введите делитель: '))
print('Ошибка при делении на 0') if n_2 == 0 else print(zero_division(n_1, n_2))
