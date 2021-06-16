class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0.0, "bonus": 0.0}


class Position(Worker):
    def get_full_name(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def get_total_income(self, wage, bonus):
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def demo(self):
        print(f'Имя: {self.name} \n'
              f'Фамилия: {self.surname} \n'
              f'Должность: {self.position} \n'
              f'Оклад: {self._income["wage"]} \n'
              f'Премия: {self._income["bonus"]}')


pos = Position()
pos.get_full_name('Иван', 'Иванов', 'Бухгалтер')
pos.get_total_income(60000, 15000)
pos.demo()
