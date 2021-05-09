import random

with open('file_ex5.txt', 'w') as f:
    [f.write(f'{random.randint(0, 100)} ') for _ in range(1000)]
with open('file_ex5.txt', 'r') as f:
    Sum = 0
    print(sum([int(x) for x in f.readline().strip().split(' ')]))
