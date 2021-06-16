"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
import random

lst = [random.randint(-100, 100) for i in range(20)]
print(lst)
max_num = lst[0]
min_num = lst[0]
max_ind = 0
min_ind = 0
for i in range(len(lst)):
    if lst[i] > max_num:
        max_num = lst[i]
        max_ind = i
    if lst[i] < min_num:
        min_num = lst[i]
        min_ind = i
lst[max_ind], lst[min_ind] = lst[min_ind], lst[max_ind]
print(lst)
