"""2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
 проходящей через эти точки."""
x1 = float(input('Введите x1: '))
y1 = float(input('Введите y1: '))
x2 = float(input('Введите x2: '))
y2 = float(input('Введите y2: '))
if x1 == x2 and y1 == y2:
    print('Координаты точек совпадают.')
else:
    if x1 == x2:
        print(f'x = {x1}')
    else:
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1
        if k == 0:
            print(f'y = {b}')
        else:
            if b > 0:
                print(f'y = {k}x + {b}')
            elif b == 0:
                print(f'y = {k}x')
            else:
                print(f'y = {k}x - {abs(b)}')
