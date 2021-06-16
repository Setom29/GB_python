"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""
max_num = 0
max_sum = 0
while True:
    num = int(input('Введите число или 0, чтобы выйти из программы: '))
    if num == 0:
        print(f'Число с максимальной суммой цифр: {max_num}\n'
              f'Сумма цифр этого числа: {max_sum}')
        break
    else:
        summ = 0
        temp = num
        while num > 0:
            summ += num % 10
            num //= 10
        if summ > max_sum:
            max_sum = summ
            max_num = temp
