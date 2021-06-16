def fact(n):
    answer = 1
    for num in range(1, n + 1):
        answer *= num
        yield answer


for el in fact(int(input('Введите число: '))):
    print(el)
