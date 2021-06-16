"""8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу."""
matrix = []
for i in range(4):
    matrix.append([])
    summ = 0
    for j in range(4):
        matrix[i].append(float(input(f'Введите элемент {i + 1} строки {j + 1} столбца: ')))
        summ += matrix[i][j]
    matrix[i].append(summ)
for line in matrix:
    for el in line:
        print(f'{el:>7}', end='')
    print('\n')
