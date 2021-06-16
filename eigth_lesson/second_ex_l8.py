class CustomError(Exception):
    def __init__(self, txt):
        self.text = txt


try:
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
    if b == 0:
        raise CustomError('Division by zero is forbidden!')
    else:
        print(a / b)
except ValueError:
    print('Invalid input.')
except CustomError as err:
    print(err)
