test_list = [7, 5, 3, 3, 2]
while True:
    elem = input('Введите элемент списка или нажмите Enter, чтобы прекратить ввод: ')
    if elem == '':
        print('Ввод элементов окончен.')
        break
    else:
        elem = int(elem)
        for i in range(len(test_list)):
            if elem > test_list[i]:
                test_list.insert(i, elem)
                break
            elif elem == test_list[i]:
                test_list.insert(i + test_list.count(test_list[i]), elem)
                break
            elif i == len(test_list) - 1:
                test_list.append(elem)

print(test_list)
