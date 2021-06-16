class Road:
    _length = 0
    _width = 0

    def __init__(self, length=5000, width=20):
        self._length = length
        self._width = width

    def asphalt_pavement(self, mass=25, height=5):
        print(f'{(self._length * self._width * mass * height) // 1000} т.')


r = Road()
r.asphalt_pavement()