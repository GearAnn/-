#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: Handler,Opener介绍.py
@time: 2018/12/3 0003 下午 6:14
"""

"""
Handler,Opener:其功能比urlopen,Request更强大，可以模拟cookie和使用代理。

"""
import urllib.request,urllib.parse

url = 'http://www.baidu.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/63.0.3239.26Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2767.400', }

# 创建handler
handler = urllib.request.HTTPHandler()
# 通过handler创建一个opener
# opener就是urlopen()的一个对象，也就是发送请求的对象
opener = urllib.request.build_opener(handler)

# 构建请求对象
request = urllib.request.Request(url, headers=headers)

# 发送请求,通过opener的open方法
response = opener.open(request)
print(response.read().decode())



















































