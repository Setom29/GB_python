from collections import ChainMap, deque
from itertools import zip_longest

string = '0123456789abcdef'
d = ChainMap({string[i]: i for i in range(len(string))}, {i: string[i] for i in range(len(string))})
print(d)


def num_to_list(num):
    while True:
        span = input(f'Введите {num} число: ').lower()
        for number in span:
            if number not in d.keys():
                print('Некорректный ввод.')
                break
        return [d[el] for el in span][::-1]


def summ(a, b):  # ok
    c = deque([x + y for x, y in zip_longest(a, b, fillvalue=0)])
    for i in range(len(c)):
        if c[i] >= 16:
            c[i] -= 16
            if i == len(c) - 1:
                c.append(1)
            else:
                c[i + 1] += 1
    return ''.join([d[el] for el in c])[::-1]


def mult(a, b):
    c = [deque([a[j] * b[i] for j in range(len(a))]) for i in range(len(b))]
    n = 0
    for el in c:
        [el.appendleft(0) for _ in range(n)]
        n += 1
    if len(c) > 1:
        temp = c[0]
        for i in range(1, len(c)):
            temp = [x + y for x, y in zip_longest(temp, c[i], fillvalue=0)]
        c = temp
    else:
        c = c[0]
    for i in range(len(c)):
        if c[i] >= 16:
            span = divmod(c[i], 16)
            c[i] = span[1]
            if i == len(c) - 1:
                c.append(span[0])
            else:
                c[i + 1] += span[0]
    if c[-1] > 15:
        span = divmod(c[-1], 16)
        c[-1] = span[1]
        c.append(span[0])
    return ''.join([d[el] for el in c])[::-1]


num1 = deque(num_to_list(1))
num2 = deque(num_to_list(2))
print(f'Сумма: {summ(num1, num2).upper()}')
print(f'Произведение: {mult(num1, num2).upper()}')
