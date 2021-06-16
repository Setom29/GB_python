test_list = [1, 40.3, 'test', [1, 2], True, {'a': 5}, {5, 3}, complex(3, 4), (5 ,5), b'test', None, ConnectionError]
for item in test_list:
    print(type(item))
