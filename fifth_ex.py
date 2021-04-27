gain = int(input('Введите сумму выручки: '))
costs = int(input('Введите сумму издержек: '))
if gain > costs:
    print('Прибыль — выручка больше издержек.')
    print(f'Рентабельность выручки:  {((gain - costs) / gain):.2}')
    people_amount = int(input('Введите количество сотрудников фирмы: '))
    print(f'Прибыль в расчёте на одного сотрудника: {((gain - costs) / people_amount):.2f}')
elif gain < costs:
    print('Убыток — издержки больше выручки.')
else:
    print('Прибыль равна нулю.')
