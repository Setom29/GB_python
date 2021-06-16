from functools import reduce
my_list = [item for item in range(100, 1001)]
print(reduce(lambda x, y: x*y, my_list))
