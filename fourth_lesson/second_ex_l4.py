full_list, answer_list = [300, 2, 12, 44, 1, 1, 4,
                          10, 7, 1, 78, 123, 55], []
[answer_list.append(full_list[i]) for i in range(1, len(full_list)) if full_list[i] > full_list[i - 1]]
print(answer_list)
