#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 绕过浏览器访问.py
@time: 2018/11/25 0025 上午 5:08
"""


"""
目的：利用python抓取网页html并保存

"""

import urllib.parse, urllib.request

word = input('输入需要抓取的内容')
url = 'http://www.baidu.com/s?'

# 把参数写成字典
data = {'ie': 'utf8', 'wd': word}

# 拼接url
query_string = urllib.parse.urlencode(data)
url = url + query_string

# 发送请求，注意：urlopen返回的是一个HTTPResponse对象
response = urllib.request.urlopen(url)
file_name = word + '.html'
with open('file_name', 'wb') as fp:
    fp.write(response.read())









