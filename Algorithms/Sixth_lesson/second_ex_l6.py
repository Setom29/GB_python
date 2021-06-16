# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
import sys
import random
from memory_profiler import profile

print(sys.version, sys.platform)


# 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)] win32

def show_sizeof(x, level=0, is_r=False):
    print("\t" * level, x.__class__, sys.getsizeof(x), '\n')
    if is_r:
        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for xx in x.items():
                    show_sizeof(xx, level + 1)
            else:
                for xx in x:
                    show_sizeof(xx, level + 1)


@profile
def first_realization():
    a = float(random.randint(-1000, 1000))
    b = float(random.randint(-1000, 1000))
    c = float(random.randint(-1000, 1000))
    if a == b and b == c:
        print('Числа равны.')
    elif b <= a <= c or c <= a <= b:
        print(f'Среднее по величине число: {a}.')
    elif a <= b <= c or c <= b <= a:
        print(f'Среднее по величине число: {b}.')
    else:
        print(f'Среднее по величине число: {c}.')
    list(map(show_sizeof, [a, b, c]))


# <class 'float'> 24 - a, b, c

@profile
def second_realization():
    # print(sorted([random.randint(-1000, 1000) for _ in range(3)])[1])
    show_sizeof(sorted([random.randint(-1000, 1000) for _ in range(3)])[1])


#  <class 'int'> 28   - хоть тут и сортируется список, но в итоге имеем 1 объект типа int
@profile
def third_realization():
    lst = tuple(sorted([random.randint(-1000, 1000) for _ in range(3)]))
    print(lst[1])
    show_sizeof(lst)


# <class 'tuple'> 64 - если нужны остальные 2 числа после работы программы, то 2 реализация не подойдет.
# Третий вариант использует кортеж для хранения данных, который занимает место меньшее чем список той же длинны.

first_realization()
second_realization()
third_realization()

# Вывод: первый вариант требует меньше всего памяти, но код для него громоздкий
# (для данной задачи это самый лучший вариант). Наиболее удобен вариант номер 2,
# так как он в одну строку дает нужный ответ, но при этом в процессе выполнения кода он требует намного больше памяти,
# чем 1 вариант. Вариант номер 3 похож на 2 вариант, но для хранения данных там используется кортеж.
