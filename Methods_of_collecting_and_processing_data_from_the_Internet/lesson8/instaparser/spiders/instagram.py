import scrapy
import re
import json
from scrapy.http import HtmlResponse
from urllib.parse import urlencode
from instaparser.items import InstaparserItem
from copy import deepcopy
import config


class InstaSpider(scrapy.Spider):
    name = 'instagram'
    allowed_domains = ['instagram.com']
    start_urls = ['https://www.instagram.com/']
    inst_login_link = '	https://www.instagram.com/accounts/login/ajax/'
    inst_login = config.inst_login
    inst_pwd = config.inst_pwd
    profiles = ['tehnokeramica', '_tatoo_o_']
    inst_api_link = 'https://www.instagram.com/api/v1/friendships/'

    def parse(self, response: HtmlResponse):
        csrf = self.fetch_csrf_token(response.text)
        yield scrapy.FormRequest(self.inst_login_link,
                                 method='POST',
                                 callback=self.login,
                                 formdata={'username': self.inst_login,
                                           'enc_password': self.inst_pwd},
                                 headers={'X-CSRFToken': csrf})

    def login(self, response: HtmlResponse):
        j_data = response.json()
        if j_data.get('authenticated'):
            for username in self.profiles:
                yield response.follow(
                    f'/{username}/',
                    callback=self.user_data_parse,
                    cb_kwargs={'username': username})

    def user_data_parse(self, response: HtmlResponse, username):
        user_id = self.fetch_user_id(response.text, username)
        max_id = 0

        url_followers = f'https://i.instagram.com/api/v1/friendships/{user_id}/followers/?count=12&search_surface=follow_list_page'
        url_following = f'https://i.instagram.com/api/v1/friendships/{user_id}/following/?count=12'

        yield response.follow(
            url_followers,
            callback=self.user_followers_parse,
            cb_kwargs={'username': username,
                       'user_id': user_id,
                       'max_id': max_id}
        )

        yield response.follow(
            url_following,
            callback=self.user_following_parse,
            cb_kwargs={'username': username,
                       'user_id': user_id,
                       'max_id': max_id}
        )

    def user_followers_parse(self, response: HtmlResponse, username, user_id, max_id):
        j_data = response.json()
        try:
            next_max_id = j_data.get('next_max_id')
        except Exception:
            next_max_id = None
        if next_max_id:
            url_followers = f'https://i.instagram.com/api/v1/friendships/{user_id}/followers/?count=12&max_id={next_max_id}&search_surface=follow_list_page'
            yield response.follow(
                url_followers,
                callback=self.user_followers_parse,
                cb_kwargs={'username': username,
                           'user_id': user_id,
                           'max_id': next_max_id}
            )

        followers = j_data.get('users')
        for el in followers:
            item = InstaparserItem(
                user_id=user_id,
                username=username,
                follow_id=el.get('pk'),
                follow_username=el.get('username'),
                photo=el.get('profile_pic_url'),
                type='follower'
            )
            yield item

    def user_following_parse(self, response: HtmlResponse, username, user_id, max_id):
        j_data = response.json()
        try:
            next_max_id = j_data.get('next_max_id')
        except Exception:
            next_max_id = None
        if next_max_id:
            url_following = f'https://i.instagram.com/api/v1/friendships/{user_id}/following/?count=12&max_id={next_max_id}'
            yield response.follow(
                url_following,
                callback=self.user_following_parse,
                cb_kwargs={'username': username,
                           'user_id': user_id,
                           'max_id': next_max_id}
            )

        following = j_data.get('users')
        for el in following:
            item = InstaparserItem(
                user_id=user_id,
                username=username,
                follow_id=el.get('pk'),
                follow_username=el.get('username'),
                photo=el.get('profile_pic_url'),
                type='following'
            )
            yield item

    def fetch_csrf_token(self, text):
        ''' Get csrf-token for auth '''
        matched = re.search('\"csrf_token\":\"\\w+\"', text).group()
        return matched.split(':').pop().replace(r'"', '')

    def fetch_user_id(self, text, username):
        matched = re.search(
            '{\"id\":\"\\d+\",\"username\":\"%s\"}' % username, text
        ).group()
        return json.loads(matched).get('id')
