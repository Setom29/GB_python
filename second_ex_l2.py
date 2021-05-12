try:
    with open('file_ex1.txt', 'r', encoding='utf-8') as f:
        line_counter = 0
        word_counter = 0
        for line in f.readlines():
            line_counter += 1
            word_counter += len(line.split(' '))
            print(f'Количество слов в {line_counter} строк = {len(line.split(" "))}')
        print(f'Количество строк = {line_counter}, \nа количество слов во всем файле = {word_counter}')
except Exception as err:
    print(err)
