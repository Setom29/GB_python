import json

try:
    with open('file_ex7.txt', 'r', encoding='utf-8') as f:
        firms_plus_av_prof_dict, firm_dict, firm_av_prof_dict, av_prof, n = [], {}, {}, 0, 0
        for line in f.readlines():
            temp = line.split(' ')
            firm_dict[temp[0]] = float(temp[2]) - float(temp[3])
            if firm_dict[temp[0]] >= 0:
                av_prof += firm_dict[temp[0]]
                n += 1
    firm_av_prof_dict['average_profit'] = av_prof / n
    firms_plus_av_prof_dict = [firm_dict, firm_av_prof_dict]
    with open('json_file_ex7.json', 'w', encoding='utf-8') as wf:
        json.dump(firms_plus_av_prof_dict, wf, indent=3, ensure_ascii=False)
except Exception as err:
    print(err)
