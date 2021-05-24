import json
from copy import deepcopy


class OfficeEquipmentStorage:
    @classmethod
    def store_equipment(cls, equipment_dict):
        equipment_dict['place'] = 'storage'
        try:
            with open('storage.json', 'r', encoding='utf-8') as eq_storage:
                temp_lst = json.load(eq_storage)
        except IOError:
            temp_lst = []
        temp_lst.append(equipment_dict)
        with open('storage.json', 'w+', encoding='utf-8') as eq_storage:
            json.dump(temp_lst, eq_storage, indent=4)

    @staticmethod
    def move_equipment():
        departments = ('Finance', 'Accounting', 'Secretariat', 'Sales', 'Purchases', 'Development', 'Quality Control',
                       'HR', 'IT', 'Storage')
        try:
            with open('storage.json', 'r', encoding='utf-8') as eq_storage:  # json file with all office equipment
                temp = json.load(eq_storage)
        except IOError:
            print('The equipment list is empty.')
            return False
        if not temp:
            print('The equipment list is empty.')
            return False
        else:
            print('List of the equipment:')
            for index, elem in enumerate(temp):
                print('-' * 20 + str(index + 1) + '-' * 20)
                for keys, values in elem.items():
                    print(f'{keys}: {values}\t')
                print('\n')
            while True:  # if equipment list isn't empty
                try:
                    num = int(input('Enter the equipment number:'))  # number of the office equipment
                    if num > len(temp) or num < 1:
                        print('Invalid number.')
                    else:
                        equipment = temp.pop(num - 1)  # equipment dict in var equipment
                        break
                except ValueError:
                    print('Not a number.')
            if 1 < int(equipment['amount']):
                while True:
                    try:
                        num = int(input(
                            f'Amount of the equipment to be moved? (max:{equipment["amount"]}) '))
                        if 1 <= num <= int(equipment["amount"]):
                            eq_amount = num
                            break
                        else:
                            print('Invalid number.')
                    except ValueError:
                        print('Not a number.')
            else:
                eq_amount = None
            while True:
                try:
                    num = int(input('Enter the division number:\n'  # trying to catch the number of division in company
                                    '1) Finance\n'
                                    '2) Accounting\n'
                                    '3) Secretariat\n'
                                    '4) Sales\n'
                                    '5) Purchases\n'
                                    '6) Development\n'
                                    '7) Quality Control\n'
                                    '8) HR\n'
                                    '9) IT\n'
                                    '10) Storage\n'))
                    if 1 <= num <= 10:
                        if eq_amount is not None:
                            max_amount = int(equipment['amount'])
                            equipment_1 = deepcopy(equipment)
                            equipment_1['amount'] = int(eq_amount)
                            equipment['amount'] -= int(eq_amount)
                            equipment_1['place'] = departments[num - 1]
                            if eq_amount != max_amount:
                                temp.append(equipment)
                            temp.append(equipment_1)
                            break
                        else:
                            equipment['place'] = departments[num - 1]
                            temp.append(equipment)
                            break
                    else:
                        print('Invalid number.')
                except ValueError:
                    print('Not a number.')
            with open('storage.json', 'w', encoding='utf-8') as eq_storage:  # json file with all office equipment
                json.dump(temp, eq_storage, indent=4)


class OfficeEquipment:
    def __init__(self):
        while True:
            try:
                temp = int(input('Amount: '))
                if temp < 1:
                    print('Invalid number.')
                else:
                    self.amount = temp
                    break
            except ValueError:
                print('Not a number.')
        self.model = input('Model: ')
        while True:
            try:
                temp = float(input('Price: '))
                if temp < 0:
                    print('Invalid number.')
                else:
                    self.price = temp
                    break
            except ValueError:
                print('Invalid value of price.')


class Printer(OfficeEquipment):
    def __init__(self):
        super().__init__()
        while True:
            temp = input('Is color? (y/n): ')
            if temp == 'y':
                self.is_color = True
                break
            elif temp == 'n':
                self.is_color = False
                break
            else:
                print('Wrong input!')
        while True:
            try:
                temp = int(input('Enter the option number:\n'
                                 '1)Inkjet printer\n'
                                 '2)Laser printer\n'))
                if temp == 1:
                    self.printer_type = 'inkjet'
                    break
                elif temp == 2:
                    self.printer_type = 'laser'
                    break
                else:
                    print('Invalid number.')
            except ValueError:
                print('Not a number.')
        self.eq_dict = {'name': 'printer', 'amount': self.amount, 'model': self.model, 'price': self.price,
                        'is_color': self.is_color,
                        'printer_type': self.printer_type}


class Scanner(OfficeEquipment):
    def __init__(self):
        super().__init__()
        while True:
            temp = input('Is color? (y/n): ')
            if temp == 'y':
                self.is_color = True
                break
            elif temp == 'n':
                self.is_color = False
                break
            else:
                print('Wrong input!')
        self.eq_dict = {'name': 'scanner', 'amount': self.amount, 'model': self.model, 'price': self.price,
                        'is_color': self.is_color}


class Laptop(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.RAM = input('RAM (ex: "8G") ')
        self.processor = input('Processor (ex: "Intel I7") ')
        self.disk = input('Disk type (ex: "HDD 1024G, SSD 256G") ')
        self.eq_dict = {'name': 'laptop', 'amount': self.amount, 'model': self.model, 'price': self.price,
                        'RAM': self.RAM,
                        'processor': self.processor, 'disk': self.disk}


class Monitor(OfficeEquipment):
    def __init__(self):
        super().__init__()

        screen_type = ('CRT', 'LCD', 'LED', 'OLED', 'QD-LED')
        while True:
            try:
                num = int(input('Screen type:\n'
                                '1) CRT\n'
                                '2) LCD\n'
                                '3) LED\n'
                                '4) OLED\n'
                                '5) QD-LED\n'))
                if 1 <= num <= 5:
                    self.screen_type = screen_type[num - 1]
                    break
                else:
                    print('Invalid number.')
            except ValueError:
                print('Not a number.')
        while True:
            try:
                num = int(input('Monitor diagonal (inches): '))
                if num > 10:
                    self.screen_diagonal = num
                    break
                else:
                    print('The monitor diagonal is too small')
            except ValueError:
                print('Not a number.')
        self.eq_dict = {'name': 'monitor', 'amount': self.amount, 'model': self.model, 'price': self.price,
                        'screen_type': self.screen_type, 'screen_diagonal': self.screen_diagonal}


while True:
    try:
        number = int(input('Write a number:\n'
                           '1) Add printer\n'
                           '2) Add scanner\n'
                           '3) Add laptop\n'
                           '4) Add monitor\n'
                           '5) Move equipment to another department\n'
                           '6) Demo\n'
                           '0) Exit\n'))
        if 0 <= number <= 6:
            if number == 1:
                eq = Printer()
                OfficeEquipmentStorage.store_equipment(eq.eq_dict)
            if number == 2:
                eq = Scanner()
                OfficeEquipmentStorage.store_equipment(eq.eq_dict)
            if number == 3:
                eq = Laptop()
                OfficeEquipmentStorage.store_equipment(eq.eq_dict)
            if number == 4:
                eq = Monitor()
                OfficeEquipmentStorage.store_equipment(eq.eq_dict)
            if number == 5:
                OfficeEquipmentStorage.move_equipment()
            if number == 6:
                try:
                    with open('storage.json', 'r', encoding='utf-8') as storage:
                        eq_lst = json.load(storage)
                    for ind, el in enumerate(eq_lst):
                        print('-' * 20 + str(ind + 1) + '-' * 20)
                        for key, value in el.items():
                            print(f'{key}: {value}\t')
                        print('\n')
                except IOError:
                    print('The equipment list is empty.')
            if number == 0:
                break
        else:
            print('Invalid number.')
    except ValueError:
        print('Not a number.')
