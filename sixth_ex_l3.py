def int_func(string):
    """принимает слова из маленьких латинских букв
    и возвращает их же, но с прописной первой буквой

    Позиционные аргументы:
    string -- строка из маленьких латинских букв

    """
    return string.title()


word_list = input('Введите строку слов: ').split(' ')
for item in word_list:
    print(int_func(item), end=' ')
