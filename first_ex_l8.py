class Date:
    def __init__(self, date):
        date = Date.rewrite_date(date)
        if Date.is_valid(date):
            self.date = date
        else:
            self.date = None

    def __str__(self):
        if self.date is not None:
            return f'{self.date[0]}.{self.date[1]}.{self.date[2]}'
        else:
            return 'Invalid date.'

    @classmethod
    def rewrite_date(cls, date):
        return date.strip().split('-')

    @staticmethod
    def is_valid(date_list):
        try:
            date_list = list(map(int, date_list))
            if len(date_list) != 3:
                return False
            if date_list[2] > 0 and 1 <= date_list[1] <= 12:
                if date_list[1] in [1, 3, 5, 7, 9, 10, 12]:
                    if 1 <= date_list[0] <= 31:
                        return True
                    else:
                        return False
                elif date_list[1] in [4, 6, 8, 11]:
                    if 1 <= date_list[0] <= 30:
                        return True
                    else:
                        return False
                else:
                    if date_list[2] % 4 != 0 or (date_list[2] % 100 == 0 and date_list[2] % 400 != 0):
                        if 1 <= date_list[0] <= 28:
                            return True
                        else:
                            return False
                    else:
                        if 1 <= date_list[0] <= 29:
                            return True
                        else:
                            return False
            else:
                return False
        except ValueError:
            return False


my_date = Date('29-02-2019')
print(my_date)
my_date = Date('29-02-2020')
print(my_date)
my_date = Date('31-08-2020')
print(my_date)
my_date = Date('31-09-2020')
print(my_date)
