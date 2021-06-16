from sys import argv

name, salary_per_hour, hours, bonus = argv
print((float(salary_per_hour) * float(hours)) + float(bonus))
