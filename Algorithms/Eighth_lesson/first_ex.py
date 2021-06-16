def handshakes(n):
    num = 0
    graph = [[True if i != j else False for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i, n):
            if j > i:
                num += int(graph[i][j])
    for el in graph:
        print(el, '\n')
    return num


print(handshakes(int(input('Введите количество друзей: '))), ' handshakes.')
