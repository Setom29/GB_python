from itertools import count, cycle, islice


def first_part_with_break():
    n = float(input('Введите целое начальное значение: '))
    for el in count(n):
        if el > n + 20:
            break
        else:
            print(el)


def first_part_without_break():
    n = float(input('Введите целое начальное значение: '))
    for el in islice(count(n), 20):
        print(el)


def second_part_with_break():
    my_list = [1, 2, 3, 4, 5, 6, 77, 8, 9, 4324, 3, 45, 3, 2, 412, 4, 12, 312, 4, 12434, 14]
    n = 0
    for el in cycle(my_list):
        n += 1
        if n > (len(my_list) * 3):
            break
        else:
            print(el)


def second_part_without_break():
    my_list = [1, 2, 3, 4, 5, 6, 77, 8, 9, 4324, 3, 45, 3, 2, 412, 4, 12, 312, 4, 12434, 14]
    for el in islice(cycle(my_list), len(my_list) * 3):
        print(el)


first_part_with_break()
print('-' * 100)
first_part_without_break()
print('-' * 100)
second_part_with_break()
print('-' * 100)
second_part_without_break()
