full_list, new_list = [2, 2, 2, 7, 23, 1, 44, 44,
                       3, 2, 10, 7, 4, 11], []
[new_list.append(item) for item in full_list if full_list.count(item) == 1]
print(new_list)
