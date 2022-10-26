import pandas as pd
import numpy as np


def prefilter_items(data, take_n_popular=5000, item_features=None):
    popularity = data.groupby('item_id')['user_id'].nunique().reset_index() / data['user_id'].nunique()
    popularity.rename(columns={'user_id': 'share_unique_users'}, inplace=True)
 
    # Уберем самые популярные товары (их и так купят)
    top_popular = popularity[popularity['share_unique_users'] > 0.2].item_id.tolist()
    data = data[~data['item_id'].isin(top_popular)]

    # Уберем самые НЕ популярные товары (их и так НЕ купят)
    top_notpopular = popularity[popularity['share_unique_users'] < 0.02].item_id.tolist()
    data = data[~data['item_id'].isin(top_notpopular)]

    # Уберем товары, которые не продавались за последние 12 месяцев
    rare_buying_items = []
    for key, val in data.groupby('item_id')['day'].min().to_dict().items():
        if val > 365:
            rare_buying_items.append(key)
    data = data[~data['item_id'].isin(rare_buying_items)]
    # Уберем не интересные для рекоммендаций категории (department)
    department_list = []
    if item_features is not None:
        for key, val in item_features.groupby('department')['item_id'].count().to_dict().items():
            if val >= 130:
                department_list.append(key)
        items_in_rare_departments = item_features[~item_features['department'].isin(department_list)]['item_id'].tolist()
        data = data[~data['item_id'].isin(items_in_rare_departments)]
    # Уберем слишком дешевые товары (на них не заработаем). 1 покупка из рассылок стоит 60 руб.
    data = data[data['sales_value'] > 1]
    # Уберем слишком дорогие товары
    data = data[data['sales_value'] < 30]
    # Возбмем топ по популярности
    top = data.groupby('item_id')['quantity'].sum().sort_values(ascending=False).head(take_n_popular).keys().tolist()
    # Заведем фиктивный item_id (если юзер не покупал товары из топ-5000, то он "купил" такой товар)
    
    data.loc[~data['item_id'].isin(top), 'item_id'] = 999999

    return data


def postfilter_items(user_id, recommednations):
    print("hello!")