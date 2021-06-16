class Stationery:  # получше использовать  title
    title = ''

    def draw(self):
        print('Drawing')


class Pen(Stationery):
    def __init__(self):
        self.title = 'Pen'

    def draw(self):
        print(f'Drawing with {self.title.lower()}')


class Pencil(Stationery):
    def __init__(self):
        self.title = 'Pencil'

    def draw(self):
        print(f'Drawing with {self.title.lower()}')


class Handle(Stationery):
    def __init__(self):
        self.title = 'Handle'

    def draw(self):
        print(f'Drawing with {self.title.lower()}')


handle = Handle()
handle.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
