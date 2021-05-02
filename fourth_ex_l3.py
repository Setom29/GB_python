def my_func(x, y):
    print(x ** y)


def my_func_1(x, y):
    x = 1 / x
    n = 1
    for _ in range(-y):
        n *= x
    print(f'{n:.08}')


my_func(2.5, -4)
my_func_1(2.5, -4)
