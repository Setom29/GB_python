from random import choice


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False
    definition = ''

    def car_info(self):
        print(f'Color: {self.color}\n'
              f'Model: {self.name}\n')

    def __init__(self, color, name, is_police, definition):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.definition = definition

    def go(self, speed):
        print(f"{self.definition} car started to move".capitalize())
        self.speed = speed

    def stop(self):
        print(f'{self.definition} car stopped'.capitalize())
        self.speed = 0

    def turn(self):
        print(f'{self.definition} car turned {choice(["right", "left"])}'.capitalize())

    def show_speed(self):
        print(f'{self.definition} car speed: {self.speed}'.capitalize())


class TownCar(Car):
    def __init__(self, color, name, is_police, definition):
        super().__init__(color, name, is_police, definition)
        print('This is the town car')

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.definition} car speed: {self.speed}.\nViolation: speeding')
        else:
            print(f'{self.definition} car speed: {self.speed}.')


class SportCar(Car):
    def __init__(self, color, name, is_police, definition):
        super().__init__(color, name, is_police, definition)
        print('This is the sport car')


class WorkCar(Car):
    def __init__(self, color, name, is_police, definition):
        super().__init__(color, name, is_police, definition)
        print('This is the work car')

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.definition} car speed: {self.speed}.\nViolation: speeding')
        else:
            print(f'{self.definition} car speed: {self.speed}.')


class PoliceCar(Car):
    def __init__(self, color, name, is_police, definition):
        super().__init__(color, name, is_police, definition)
        print('This is the police car')


p_car = PoliceCar('black&white', 'Ford', True, 'Police')

p_car.go(60)
p_car.turn()
p_car.show_speed()
p_car.stop()
s_car = SportCar('red', 'Ferrari', False, 'Sport')
s_car.go(60)
s_car.turn()
s_car.stop()
w_car = WorkCar('blue', 'Volvo', False, 'Work')
w_car.go(70)
w_car.show_speed()
w_car.stop()
t_car = TownCar('green', 'Mercedes', False, 'Town')
t_car.go(100)
t_car.show_speed()
t_car.stop()
t_car.car_info()