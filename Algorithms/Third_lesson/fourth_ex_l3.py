"""4. Определить, какое число в массиве встречается чаще всего."""
import random

lst = [random.randint(-10, 10) for i in range(100)]
print(lst)
num_dict = {}  # словарь, состоящий из пар {число: сколько раз встречалось, ...}
for el in lst:
    if el in num_dict:
        num_dict[el] += 1
    else:
        num_dict[el] = 1
print(num_dict)
max_amount = 0
num = 0
for key, value in num_dict.items():
    if value >= max_amount:
        num = key
        max_amount = value
for key, value in num_dict.items():  # если таких чисел несколько, вывести все
    if value == max_amount:
        print(f'Число {key}\n'
              f'Количество в списке {value}\n')
