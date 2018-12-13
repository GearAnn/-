#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: url异常处理.py
@time: 2018/12/3 0003 下午 5:51
"""
"""
url的异常（URLError）处理

URLError原因:
(1)没有网
(2)服务器连接失败
(3)找不到指定的服务器

URLError/HTTPError这两个类都属于urllib.error
HTTPError是URLError的子类

"""

import urllib.request,urllib.parse,urllib.error

# 随便乱写一个不存在url
url = 'http://www.maodan.com/'

# 用 try Exception来测试捕获
# try:
#     response = urllib.request.urlopen(url)
#     print(response)
# except NameError as e:
#     print(e)
# 结果：异常捕获不了，因为URLError不是NameError类型,所有要用URLError来捕获

try:
    response = urllib.request.urlopen(url)
    print(response)
except urllib.error.HTTPError as e:
    print(e)
except urllib.error.URLError as e:
    print(e)

# 注意：如果HTTP和URL的异常需要同时捕获的时候，把HTTPError写在前面，因为URLError是父类，父类范围更大


















