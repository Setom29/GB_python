"""https://habr.com/ru/post/133037/"""
import math
import cProfile


def sieve(num):
    # ищем числа не от 2 * i, а от i ** 2/ последнее число, на котором стоит закончить процесс высеивания: k = sqrt(n)
    # так как границы поиска не оговаривались, то верхней границей будет переданное число, умноженное на 100.
    num_lst = [1 for _ in range(0, num * 100)]
    n = len(num_lst)
    num_lst[0], num_lst[1] = 0, 0
    for i in range(0, int(math.sqrt(n)) + 1):
        if num_lst[i] != 0:
            j = i ** 2
            while j <= n - 1:
                num_lst[j] = 0
                j += i
    return [i for i in range(n) if num_lst[i] == 1][num - 1]


# "second_ex_l4.sieve(10)"
# 1000 loops, best of 5: 389 usec per loop

# "second_ex_l4.sieve(50)"
# 1000 loops, best of 5: 2.09 msec per loop

# "second_ex_l4.sieve(100)"
# 1000 loops, best of 5: 4.34 msec per loop

# "second_ex_l4.sieve(200)"
# 1000 loops, best of 5: 10 msec per loop

# "second_ex_l4.sieve(1000)"
# 1000 loops, best of 5: 53.2 msec per loop

def prime(num):
    i = 1
    lst = []
    while True:
        i += 1
        flag = True
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                flag = False
        if flag:
            lst.append(i)
            if len(lst) == num:
                return i

# "second_ex_l4.prime(10)"
# 1000 loops, best of 5: 23.9 usec per loop


# "second_ex_l4.prime(50)"
# 1000 loops, best of 5: 315 usec per loop

# "second_ex_l4.prime(100)"
# 1000 loops, best of 5: 984 usec per loop

# "second_ex_l4.prime(200)"
# 1000 loops, best of 5: 2.75 msec per loop

# "second_ex_l4.prime(1000)"
# 1000 loops, best of 5: 40.3 msec per loop


# cProfile.run('sieve(100000)') 5.986 seconds
# cProfile.run('prime(100000)')  88.604 seconds
