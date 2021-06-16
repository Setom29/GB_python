import sys
import random
from memory_profiler import profile
from collections import deque
print(sys.version, sys.platform)
# 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)] win32
"""2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа."""


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
    tpl = tuple(random.randint(255, 1000) for _ in range(100000))
    show_sizeof(tpl)
    # print([i for i in range(len(tpl)) if tpl[i] % 2 == 0])


# <class 'tuple'> 800040 - tpl, где каждый элемент занимает 8 байт
# Наилучший из представленных вариантов по использованию памяти, так как он хранит в памяти только кортеж tpl,
# который весит меньше, чем список той же длинны.
@profile
def second_realization():
    lst = [random.randint(255, 1000) for _ in range(100000)]
    # print(f'lst = {lst}')
    even_lst = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_lst.append(i)
    # print(f'even_lst = {even_lst}')
    show_sizeof(lst)
    show_sizeof(even_lst)


# <class 'list'> 824456 - список занимает меньше памяти, чем очередь, но больше чем кортеж того же размера.
# <class 'list'> 406488 - even_lst
# Использование списка для вывода увеличивает затраты памяти.

@profile
def third_realization():
    deq = deque([random.randint(255, 1000) for _ in range(100000)])
    # print(f'deque = {deq}')
    even_deq = deque()
    for i in range(len(deq)):
        if deq[i] % 2 == 0:
            even_deq.append(i)
    # print(even_deq)
    show_sizeof(deq)
    show_sizeof(even_deq)


# <class 'collections.deque'> 825360 - очередь требует больше всего памяти, поэтому данный вариант будет самым
# затратным из представленных.
# <class 'collections.deque'> 412992 - очередь even_deq

first_realization()
second_realization()
third_realization()

# for el in first_realization.__code__.co_varnames[-1]:
#     print(f"Size of {el} == {sys.getsizeof(eval('el'))}, {el} value at the end of the program == {eval('el')}")

# Вывод: первый вариант требует меньше всего памяти, так как там был использован кортеж.
# В двух других вариантах использовались list и deque,
# # которые требуют больше памяти, а это изменяемые объекты.
