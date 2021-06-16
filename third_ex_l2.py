month_dict = {'Зима': [12, 1, 2],
              'Весна': [3, 4, 5],
              'Лето': [6, 7, 8],
              'Осень': [9, 10, 11]}
month_number = int(input('Введите номер месяца: '))
for key, value in month_dict.items():
    if month_number in value:
        print(key)
