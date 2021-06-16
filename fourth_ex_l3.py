def is_required_type(x, y):
    if (type(x) == float or type(x) == int) and (type(y) == int and y < 0):
        return True
    else:
        return False


def my_func(x, y):
    if is_required_type(x, y):
        print(x ** y)
    else:
        print('Value error!')


def my_func_1(x, y):
    if is_required_type(x, y):
        x = 1 / x
        n = 1
        for _ in range(-y):
            n *= x
        print(f'{n:.08}')
    else:
        print('Value error!')


my_func(2.5, -4)
my_func_1(2.5, -4)
