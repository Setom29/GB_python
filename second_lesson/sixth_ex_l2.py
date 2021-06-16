# products_list = [(1, {'Название': 'сканер', 'Цена': '2000', 'Количество': '5', 'Ед. изм.': 'шт.'}), (2, {'Название':
# 'принтер', 'Цена': '2500', 'Количество': '6', 'Ед. изм.': 'шт.'})]
counter = 0  # количество товаров
products_list = []  # для всех товаров
dict_of_categories = {'Название': [], 'Цена': [], 'Количество': [], 'Ед. изм.': []}  # для аналитики товара
while True:
    elem = input('Введите название товара или нажмите Enter, чтобы прекратить ввод: ')
    if elem == '':
        break
    else:
        counter += 1
        prod_dict = {'Название': elem, 'Цена': float(input(f'Введите цену товара: ')),
                     'Количество': int(input(f'Введите количество товара: ')),
                     'Ед. изм.': input(f'Введите единицу измерения товара: ')}  # словарь товара
        products_list.append((counter, prod_dict))

for item in products_list:  # заполнение словаря категорий
    for key, value in item[1].items():
        if value not in dict_of_categories[key]:
            dict_of_categories[key].append(value)
for item in products_list:
    print(item)
for key, value in dict_of_categories.items():
    print(f'{key}:{value}')
