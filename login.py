#!/usr/bin/env python
'''
# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 14:04
# @Author  : YzzHA
# @email   : 18390955482@163.com
# @File    : login.py
# @Software: PyCharm
# @desc    : Ding E applies QuickStart in Python
'''

import json
import requests

class Login():
    def __init__(self, auth_code = ''):
        self.auth_code = auth_code
        self.config = self.get_config_data('config.json')

    def get_data(self):
        data = self.get_user()
        if ('errcode' in data): # Access IP is not on the whitelist
            print("fail code: %s" % data['errcode'])

        print(data) # check response
        return data

    def get_token(self, url = '/gettoken'):
        token = requests.get(self.config['weburl'] + url, params=self.config['app']).json()
        self.token = token['access_token']

        return self.token

    def get_userinfo(self, url = '/user/getuserinfo'):
        data = {
            "access_token": self.get_token(),
            "code": self.auth_code
        }
        userinfo = requests.get(self.config['weburl'] + url, params=data).json()

        return userinfo

    def get_user(self, url = '/user/get'):
        userinfo = self.get_userinfo()
        if ('userid' not in userinfo):
            return userinfo
        data = {
            "access_token": self.token,
            "userid": userinfo['userid']
        }
        user = requests.get(self.config['weburl'] + url, params=data).json()

        return {
            "result": {
                "userId": userinfo['userid'],
                "userName": user["name"]
            }
        }

    # Read json file
    def get_config_data(self, url = ""):
        with open(url, 'r') as f:
            data = json.loads(f.read())

        return data

