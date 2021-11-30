from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as err
import time
import datetime
from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
db = client['letters']


def to_db(letters):
    counter = 0
    for letter in letters:
        counter += 1
        db.letters.insert_one(letter)
    print(f'\nВ базу добавлено {counter} писем.')


months = {'января': '01', 'февраля': '02', 'марта': '03', 'апреля': '04', 'мая': '05', 'июня': '06', 'июля': '07',
          'августа': '08', 'сентября': '09', 'октября': '10', 'ноября': '11', 'декабря': '12'}
driver = webdriver.Firefox(executable_path='./geckodriver')
driver.implicitly_wait(10)
driver.get('https://mail.ru')

# mail.ru authorization start
elem = driver.find_element(By.XPATH, '//div[contains(@class, "email-input-container")]//input[@type="text"]')
elem.send_keys('study.ai_172@mail.ru')
elem.send_keys(Keys.ENTER)
elem = driver.find_element(By.CLASS_NAME, 'password-input')
time.sleep(5)
elem.send_keys('NextPassword172#')
elem.send_keys(Keys.ENTER)
# mail.ru authorization end
time.sleep(7)
elem = driver.find_element(By.XPATH, "//div[@class='dataset__items']/a[1]")
elem.click()  # click on the first letter

letters = []
while True:
    try:
        letter = {}
        time.sleep(0.7)
        letter['text'] = driver.find_element(By.XPATH, "//div[@class='letter__body']/div[@class='letter-body']").text
        letter['topic'] = driver.find_element(By.XPATH, "//h2[@class='thread__subject']").text
        letter['contact'] = driver.find_element(By.XPATH,
                                                "//div[@class='letter__author']/span[@class='letter-contact']").text
        date = driver.find_element(By.XPATH, "//div[@class='letter__date']").text
        date = date.split(', ')[0]
        if date == 'Вчера':
            date = (datetime.datetime.today() - datetime.timedelta(days=1)).date()
        elif date == 'Сегодня':
            date = datetime.datetime.today()
        else:
            date = date.split()
            if len(date) == 2:
                date.append(str(datetime.datetime.now().year))
            date[1] = months[date[1]]
            date = '-'.join(date)
            date = datetime.datetime.strptime(date, '%d-%m-%Y').date()
        letter['date'] = str(date)
        letters.append(letter)
        elem = driver.find_element(By.XPATH,
                                   '//div[@class="portal-menu__group"]//span[contains(@class, "button2_arrow-down")]')
        elem.click()
    except err.ElementClickInterceptedException as err_click:
        print(err_click)
        break
    except Exception as exception:
        print(exception)
        elem = driver.find_element(By.XPATH,
                                   '//div[@class="portal-menu__group"]//span[contains(@class, "button2_arrow-down")]')
        elem.click()
        continue

to_db(letters)
