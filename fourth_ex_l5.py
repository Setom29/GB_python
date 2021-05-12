try:
    with open('file_ex4.txt', 'r', encoding='utf-8') as f:
        my_list = ['Один', 'Два', 'Три', 'Четыре']
        with open('new_file_ex4.txt', 'w', encoding='utf-8') as wf:
            for line in f.readlines():
                temp = line.split(' ')
                temp[0] = my_list[int(temp[2]) - 1]
                wf.write(f'{temp[0]} {temp[1]} {temp[2]}')
except Exception as err:
    print(err)
