from random import randint
from collections import Counter


def graph_generator(num):  # функция генерирует граф, используя возможности модуля random.
    graph = {i + 1: [] for i in range(num)}
    if num == 1:
        return {1: []}
    else:
        for i in range(num):
            node_list = []
            for _ in range(randint(num // 2, num)):  # определяем сколько узлов будет связано с текущей
                error = 0
                while True:
                    span_num = randint(1, num)  # записываем узлы, выбранные через randint
                    if span_num not in node_list and span_num != i + 1:
                        # исключаем запись повторений и номера текущего узла
                        node_list.append(span_num)
                        break
                    else:  # если количество повторений будет равно количеству узлов, то выходим из цикла while
                        if error >= num:
                            break
                        else:
                            error += 1
            graph[i + 1] = sorted(node_list)  # отсортируем граф
        node_amount = Counter(''.join([''.join(map(str, el)) for el in graph.values()]))
        # посчитаем количество попаданий каждого из узлов в граф
        for el in node_amount:
            if node_amount[el] == 0:
                # если существует узел el, с которым связи нет, то добавляе связь первого узла и el
                graph[1].append(int(el))
        return graph


def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            dfs(graph, k, visited)
    return visited


n = int(input('Введите количество узлов: '))
graph1 = graph_generator(n)
print(f'Граф в виде списка смежности: {graph1}')
print('Посещенные вершины:', dfs(graph1, 2, []))
