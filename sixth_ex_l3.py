def int_func(string):
    flag = True
    for letter in string:
        if ord(letter) > 122 or ord(letter) < 97:
            flag = False
    if flag:
        return string.title()


word_list = input('Введите строку слов: ').split(' ')
output_list = []
for item in word_list:
    item = int_func(item)
    if item is not None:
        output_list.append(item)
print(*output_list)
