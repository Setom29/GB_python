"""1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных
подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(),
sha1() или любой другой из модуля hashlib задача считается не решённой."""

import hashlib
from collections import Counter


def subs_count(string):
    subs = []
    len_string = len(string)
    for i in range(len_string + 1):
        for j in range(i + 1, len_string + 1):
            sub_s = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            subs.append(sub_s)
    subs = Counter(subs)
    subs.pop(hashlib.sha1(string.encode('utf-8')).hexdigest())
    return len(subs)


s = input('Введите строку: ')
print(f'В строке "{s}" {subs_count(s)} подстрок.')
