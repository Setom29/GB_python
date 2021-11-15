import json
import requests

"""1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, 
сохранить JSON-вывод в файле *.json."""

username = 'Setom29'
url = f"https://api.github.com/users/{username}/repos"

req = requests.get(url).json()

if 'id' not in req[0]:
    print(f'No user: {username}')
else:
    repo = [el['name'] for el in req]

    with open(f'{username}_repos.json', 'w') as f:
        json.dump(repo, f)
