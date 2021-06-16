from collections import namedtuple, defaultdict, deque

firm = namedtuple('firm', 'name one two three four')
firm_dict = defaultdict(float)
firm_lst = []
deq = deque([None])
av_prof = 0
while True:
    try:
        n = int(input('Введите колличество предприятий: '))
        break
    except ValueError:
        print('Некорректный ввод.')
for i in range(n):
    span = [input('Введите названия предприятия: ')]
    for j in range(1, 5):
        while True:
            try:
                span.append(float(input(f'Введите доход за {j} квартал: ')))
                break
            except ValueError:
                print('Некорректный ввод.')
    firm_lst.append(firm._make(span))

for el in firm_lst:
    span = el.one + el.two + el.three + el.four
    av_prof += span
    firm_dict[el.name] = span
av_prof = round(av_prof / n, 2)
for key, value in firm_dict.items():
    if value >= av_prof:
        deq.append(key)
    else:
        deq.appendleft(key)
print(f'Средняя прибыль: {av_prof}.')
print('Доход ниже среднего')
for _ in range(len(deq)):
    span = deq.popleft()
    if span is None:
        print('Доход выше среднего: ')
    else:
        print(span)


