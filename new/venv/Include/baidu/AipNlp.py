#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: AipNlp.py
@time: 2018/10/20 17:20
'''

from aip import AipNlp
if __name__ == "__main__":
    """ 你的 APPID AK SK """
    APP_ID = '14494753'
    API_KEY = '7ANhhaOxKwfH4opIKa1bEbj1'
    SECRET_KEY = 'yx1D7tUmul8Gx5CU4kglPTqqUMmzBgz4'

    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

    text = "百度是一家高科技公司"

    """ 调用词法分析 """
    print(client.lexer(text))