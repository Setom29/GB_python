class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        matr_string = ''
        for el in self.matr:
            matr_string += f'{" ".join(str(x) for x in el)}\n'
        return matr_string

    def __add__(self, other):
        return Matrix(
            [[self.matr[i][j] + other.matr[i][j] for i in range(len(self.matr))] for j in range(len(other.matr))])


A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
print(A + B)
