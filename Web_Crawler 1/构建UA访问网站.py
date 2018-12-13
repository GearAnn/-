#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: 构建UA访问网站.py
@time: 2018/11/25 0025 上午 8:56
"""

"""
建立请求头部信息：用Python伪造User-Agent 模拟其他浏览器(谷歌浏览器等)访问服务端。
"""

import urllib.request
import urllib.parse

url = 'http://www.taobao.com/'

# 1.构建header头部信息,打开Fiddler，拿到‘淘宝’的 User-Agent
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/70.0.3538.102 Safari/537.36'}

# 2.构建请求对象
request = urllib.request.Request(url=url, headers=header)

# 3.发送请求
request = urllib.request.urlopen(request)

print(request.read().decode())




