class ComplexNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return ComplexNum(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNum(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __str__(self):
        if self.re == 0:
            return f'{round(self.im, 7)}j'
        elif self.im == 0:
            return f'{round(self.re, 7)}'
        else:
            if self.im < 0:
                return f'{round(self.re, 7)} - {round(abs(self.im), 7)}j'
            else:
                return f'{round(self.re, 7)} + {round(self.im, 7)}j'


complex_list_1 = [ComplexNum(*el) for el in [[1, 2], [1, -4], [0, -5], [3, 0]]]
complex_list_2 = [ComplexNum(*el) for el in [[1, -2], [1, -4], [5, -7.6]]]
print('-' * 20 + '+' + '-' * 20)
for i in range(len(complex_list_1)):
    for j in range(len(complex_list_2)):
        print(f'({complex_list_1[i]}) + ({complex_list_2[j]}) = {complex_list_1[i] + complex_list_2[j]}')
print('-' * 20 + '*' + '-' * 20)
for i in range(len(complex_list_1)):
    for j in range(len(complex_list_2)):
        print(f'({complex_list_1[i]}) * ({complex_list_2[j]}) = {complex_list_1[i] * complex_list_2[j]}')
