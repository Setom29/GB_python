test_list = input().split(' ')
for index, string in enumerate(test_list):
    if len(string) > 10:
        string = string[0:10]
    print(f'{index + 1}) {string}')
