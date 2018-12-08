#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: main.py
@time: 2018/10/11 15:43
'''

import urllib.request
from Handlejs import Py4Js
import sys


def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8')
    return data
def translate(content, tk):
    if len(content) > 4891:
        print("翻译的长度超过限制！！！")
        return
    content = urllib.parse.quote(content)
    url = "http://translate.google.cn/translate_a/single?client=t" + "&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" + "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" + "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (
    tk, content)
    result = open_url(url)
    end = result.find("\",")
    if end > 4:
        return result[4:end].encode('utf-8')
def main(content):
    js = Py4Js()
    tk = js.getTk(content)
    return translate(content, tk)

if __name__ == "__main__":
	sys.setde
    print(main(sys.argv[1]))
    # print(main("hello").decode('utf-8'))
