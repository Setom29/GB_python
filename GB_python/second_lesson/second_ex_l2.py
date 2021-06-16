test_list = []
while True:
    elem = input('Введите элемент списка или нажмите Enter, чтобы прекратить ввод: ')
    if elem == '':
        print('Ввод элементов окончен.')
        break
    else:
        test_list.append(elem)
for i in range(0, len(test_list) - len(test_list) % 2, 2):
    test_list[i], test_list[i + 1] = test_list[i + 1], test_list[i]
print(test_list)
