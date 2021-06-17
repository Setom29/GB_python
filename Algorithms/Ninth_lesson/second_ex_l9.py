from collections import Counter, deque

codes = dict()


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def get_code(tree, path=''):
    if not isinstance(tree, Node):
        codes[tree] = path
    else:
        get_code(tree.left, path=f'{path}0')
        get_code(tree.right, path=f'{path}1')


def get_tree(string):
    assert len(string) > 0, 'Строка слишком короткая.'
    string_count = Counter(string)
    sort_s = deque(sorted(string_count.items(), key=lambda item: item[1]))  # В очередь записываем значения словаря,
    # отсортированные по частоте вхождения в строку
    while len(sort_s) > 1:
        weight = sort_s[0][1] + sort_s[1][1]  # вычисляем сумму частот
        node = Node(left=sort_s.popleft()[0], right=sort_s.popleft()[0])  # формируем узел

        for i, el in enumerate(sort_s):
            # в зависимости от значения переменной weight вставляем узел на нужное место в очереди
            if weight > el[1]:
                continue
            else:
                sort_s.insert(i, (node, weight))
                break
        else:
            sort_s.append((node, weight))

    return sort_s[0][0]


string = input('введите строку: ')

get_code(get_tree(string))
for el in Counter(string).items():
    print(f'Символ: {el[0]}, частота: {el[1]}, код: {codes[el[0]]}')
for i in string:
    print(codes[i], end=' ')
