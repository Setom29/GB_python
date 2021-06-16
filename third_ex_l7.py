class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return Cell(int(self.cell + other.cell))

    def __mul__(self, other):
        return Cell(int(self.cell * other.cell))

    def __sub__(self, other):
        if self.cell > other.cell:
            return Cell(int(self.cell - other.cell))
        else:
            return 'Subtraction error'

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def __str__(self):
        return f'Number of cells: {self.cell}'

    def make_order(self, num):
        div, mod = divmod(self.cell, num)
        return '\n'.join(['*' * num for _ in range(div)]) + '\n' + '*' * mod


cell_1 = Cell(6)
cell_2 = Cell(15)
cell_3 = Cell(50)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_3 / cell_1)
print(cell_3.make_order(9))
