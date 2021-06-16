"""4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры."""
from cProfile import run
import timeit


def series(num):
    summ, n = 0, 1
    for i in range(num):
        summ += n
        n /= -2
    return summ


# "first_ex_l4.series(10)"
# 1000 loops, best of 5: 1.31 usec per loop

# "first_ex_l4.series(100)"
# 1000 loops, best of 5: 10.4 usec per loop

# "first_ex_l4.series(500)"
# 1000 loops, best of 5: 51 usec per loop

# "first_ex_l4.series(1000)"
# 1000 loops, best of 5: 117 usec per loop

# "first_ex_l4.series(100000)"
# 1000 loops, best of 5: 12.8 msec per loop


def rec_series(num):
    if num == 1:
        return 1
    return 1 / ((-2) ** (num - 1)) + rec_series(num - 1)


# "first_ex_l4.rec_series(10)"
# 1000 loops, best of 5: 4.4 usec per loop

# "first_ex_l4.rec_series(100)"
# 1000 loops, best of 5: 81 usec per loop

# "first_ex_l4.rec_series(500)"
# 1000 loops, best of 5: 697 usec per loop

# 10/1    0.000    0.000    0.000    0.000 first_ex_l4.py:28(rec_series) 10
# 100/1    0.000    0.000    0.000    0.000 first_ex_l4.py:28(rec_series) 100
# 500/1    0.001    0.000    0.001    0.001 first_ex_l4.py:28(rec_series) 500
# 993 : Recursion error

def generator_sum(num):
    return sum((-2) ** -i for i in range(0, num))

run('generator_sum(10000000)')
# "first_ex_l4.generator_sum(10)"
# 1000 loops, best of 5: 3.39 usec per loop

# "first_ex_l4.generator_sum(100)"
# 1000 loops, best of 5: 29.5 usec per loop

# "first_ex_l4.generator_sum(500)"
# 1000 loops, best of 5: 152 usec per loop

# "first_ex_l4.generator_sum(1000)"
# 1000 loops, best of 5: 314 usec per loop

# "first_ex_l4.generator_sum(100000)"
# 1000 loops, best of 5: 35.7 msec per loop

# 11 0.000 0.000 0.000 0.000 first_ex_l4.py: 52( < genexpr >) (10)
# 101 0.000 0.000 0.000 0.000 first_ex_l4.py: 52( < genexpr >) (100)
# 501 0.000 0.000 0.000 0.000 first_ex_l4.py: 52( < genexpr >) (500)
# 1001 0.000 0.000 0.000 0.000 first_ex_l4.py: 52( < genexpr >) (1000)
# 100001 0.054 0.000 0.054 0.000 first_ex_l4.py: 52( < genexpr >) (100000)