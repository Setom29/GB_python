try:
    with open('file_ex2.txt', 'r') as f:
        line_counter = 0
        word_counter = 0
        for line in f.readlines():
            line_counter += 1
            word_counter += len(line.split(' '))
        print(f'Количество строк = {line_counter}, а количество слов = {word_counter}')
except Exception as err:
    print(err)
