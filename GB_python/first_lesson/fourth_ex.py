max_num = 0
num = int(input("Введите целое положительное число: "))
while num > 0:
    n = num % 10
    num = num // 10
    if n >= max_num:
        max_num = n
    else:
        continue
print(max_num)
