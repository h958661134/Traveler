#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: Post.py
@time: 2018/10/10 19:51
'''

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver


if __name__ == "__main__":
    driver=webdriver.Firefox()
    driver.maximize_window()
    url="https://translate.google.cn/#zh-CN/en/"
    with open("a.txt", "w", encoding='utf-8') as a:
        with open("ch.txt",encoding='utf-8') as f:
            for line in f:
                end=line.strip('\n')
                urls=url+end
                driver.get(urls)
                data=driver.page_source
                soup=bs(data,"lxml")
                a.write(soup.select("#result_box")[0].text+"\n")
