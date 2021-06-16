try:
    with open('file_ex3.txt', 'r', encoding='utf-8') as f:
        sum_list = [0, 0]
        for line in f.readlines():
            temp = line.split(' ')
            temp[1] = temp[1].replace('\n', '')
            if float(temp[1]) < 20000:
                print(temp[0])
            sum_list[0] += float(temp[1])
            sum_list[1] += 1
        print('Средняя зарплата =', round(sum_list[0] / sum_list[1], 2))
except Exception as err:
    print(err)
