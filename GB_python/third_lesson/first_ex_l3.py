def zero_division(p_1, p_2):
    """Выводит на экран частное от деления.

    Позиционные аргументы:
    p_1 -- делимое
    p_2 --  делитель

    """
    try:
        print(p_1 / p_2)
    except ZeroDivisionError:
        print('Zero division error!')


zero_division(float(input('Введите делимое: ')), float(input('Введите делитель: ')))
