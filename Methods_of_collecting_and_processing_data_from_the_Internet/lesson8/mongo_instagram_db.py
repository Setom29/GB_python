from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client['instagram_db']
for username in ['tehnokeramica', '_tatoo_o_']:
    users = db[username]

    print(f'Подписчики пользователя {username}:')
    user_followers = users.find({'type': 'follower'})
    for user in user_followers:
        pprint(user)

    print(f'Подписки пользователя {username}:')
    user_following = users.find({'type': 'following'})
    for user in user_following:
        pprint(user)
