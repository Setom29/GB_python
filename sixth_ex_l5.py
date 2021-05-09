try:
    with open('file_ex6.txt', 'r', encoding='utf-8') as f:
        subject_dict = {}
        for line in f.readlines():
            subject_name, subject_hours = line.split(':')
            subject_hours = subject_hours.strip()
            for it in subject_hours:  # убираем лишние символы
                if it.isdigit() or it == ' ':
                    continue
                else:
                    subject_hours = subject_hours.replace(it, '')
            subject_dict[subject_name] = sum(list(map(int, subject_hours.strip().split(' '))))
    print(subject_dict)
except Exception as err:
    print(err)
