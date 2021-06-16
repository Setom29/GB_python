"""1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов."""
lst_2 = [i for i in range(2, 10)]
num_dict = dict(zip(tuple(lst_2), [0 for i in range(len(lst_2))]))
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            num_dict[j] += 1
for key, value in num_dict.items():
    print(f'{key}: {value}\n', end='')
