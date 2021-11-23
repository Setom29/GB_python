import bs4
import requests
from pymongo import MongoClient
import pandas as pd
import re

client = MongoClient('127.0.0.1', 27017)

db = client['vacancies']


def processing_data(soup):
    vacs = soup.find_all('div', {"class": "vacancy-serp-item"})
    vacs_list = []
    for vac in vacs:
        vac_dict = {}

        # name
        name = vac.find("span", {"class": "g-user-content"}).text
        vac_dict['name'] = name

        # company
        company = vac.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'})
        vac_dict['company'] = company.text
        # salary
        salary = vac.find('div', {'class': 'vacancy-serp-item__sidebar'})

        # salary = re.split(r'\s|-', salary)
        if not salary:
            salary_min = None
            salary_max = None
            salary_currency = None
        else:
            try:
                salary = salary.text.replace('\u202f', '')
                salary = salary.split(' ')
                if salary[1] == '–':
                    salary_min = int(salary[0])
                    salary_max = int(salary[2])
                elif salary[0] == 'до':
                    salary_min = None
                    salary_max = int(salary[1])
                elif salary[0] == 'от':
                    salary_min = int(salary[1])
                    salary_max = None

                salary_currency = salary[-1]
            except Exception as err:
                salary_min = None
                salary_max = None
                salary_currency = None
        #         vacancy_dict['salary'] = salary
        vac_dict['salary_min'] = salary_min
        vac_dict['salary_max'] = salary_max
        vac_dict['salary_currency'] = salary_currency

        # link
        link = vac.find("a", {"data-qa": "vacancy-serp__vacancy-title"})['href'].split('?')[0]
        vac_dict['link'] = link

        # source
        vac_dict['source'] = 'hh.ru'
        vacs_list.append(vac_dict)
    return vacs_list


def scan_hh(vac):
    params = {
        'text': vac,
        'search_field': 'name',
        'area': '',
        'salary': '',
        'currency_code': 'RUR',
        'experience': 'doesNotMatter',
        'order_by': 'relevance',
        'search_period': '0',
        'items_on_page': '100',
        'no_magic': 'true',
        'L_save_area': 'true',
        'page': '0'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'
    }
    url = 'https://hh.ru/search/vacancy/'
    vacs_list = []
    while True:
        data = requests.get(url, params=params, headers=headers)
        if str(data) == '<Response [200]>':
            soup = bs4.BeautifulSoup(data.text, 'html.parser')
        else:
            print(str(data))
            break
        vacs_list.extend(processing_data(soup))
        if soup.find('a', {'data-qa': 'pager-next'}) is None:
            break
        else:
            params['page'] = str(int(params['page']) + 1)
    print(f'\n{len(vacs_list)} found')
    return vacs_list


def to_db(vacancies):
    counter = 0
    for vacancy in vacancies:
        if len([elem for elem in db.vacancies.find({'link': vacancy['link']})]) == 0:
            db.vacancies.insert_one(vacancy)
            counter += 1
    print(f'\nВ базу добавлено {counter} вакансий.')
