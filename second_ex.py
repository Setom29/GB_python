string = input('Введите время в секундах: ')
hours = int(string) // 3600
minutes = (int(string) - hours * 3600) // 60
seconds = (int(string) - minutes * 60 - hours * 3600) % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')
