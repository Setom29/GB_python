from pymongo import MongoClient
from pprint import pprint
import parsing as pr

client = MongoClient('127.0.0.1', 27017)
db = client['vacancies']


def update_db():
    """
    Добавляет в базу данных вакансии по запросу.
    Если такая вакансия в базе уже существует, запись не добавляется.
    """
    vac_name = input('Vacancy: ')
    vacancies = pr.scan_hh(vac_name)
    pr.to_db(vacancies)


def find_in_db():
    """
    Печатает список вакансий по запросу мин зарплаты
    """
    min_salary_request = int(input('Укажите нижнюю границу зарплаты: '))
    curr = input('Укажите валюту: \n1) "руб." \n2) "USD" \n3) "EUR"\n')
    if curr == '1':
        curr = 'руб.'
    elif curr == '2':
        curr = 'USD'
    elif curr == '3':
        curr = 'EUR'
    else:
        print('Currency error.')
        return
    for vacancy in db.vacancies.find({'$or':
                                          [{'$and': [{'salary_min': {'$gte': min_salary_request}, 'salary_currency':curr}, {'salary_max': None}]},
                                           {'salary_max': {'$gte': min_salary_request}, 'salary_currency':curr}]}):
        pprint(vacancy)


update_db()
find_in_db()
