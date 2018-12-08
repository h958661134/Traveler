#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: urls.py
@time: 2018/6/2 18:20
'''

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # 配置成功之后去booktest的urls文件中找对应的视图函数
    url(r'^',include('demo1.urls'))
]