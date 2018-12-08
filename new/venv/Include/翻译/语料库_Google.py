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
    url = "http://translate.google.cn/translate_a/single?client=t" + "&sl=zh-CN&tl=en&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" + "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" + "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (
    tk, content)
    result = open_url(url)
    end = result.find("\",")
    if end > 4:
        return result[4:end]
def main(content):
    js = Py4Js()
    tk = js.getTk(content)
    return translate(content, tk)

if __name__ == "__main__":
    # with open("output_english.txt","w",encoding='utf-8') as f:
    #     with open("input_chinese.txt",encoding='utf-8') as f1:
    #         for line in f1:
    #             content=line.strip("\n")
    #             f.write(content+"   "+main(content)+"\n")
    print(main(sys.argv[1]))
