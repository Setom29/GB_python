with open('file_ex1.txt', 'w', encoding='utf-8') as f:
    while True:
        temp = input('Введите данные')
        if temp == '':
            break
        else:
            f.write(temp + '\n')
