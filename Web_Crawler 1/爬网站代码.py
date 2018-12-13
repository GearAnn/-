#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: urllib利用.py
@time: 2018/11/25 0025 上午 3:40
"""
'''
urllib库: 模拟浏览器发送请求的库，Python在setting里面安装。

引入: 
urllib.request(url信息获取)
urllib.parse(url解析)

主要利用2个方法： 
urlopen
urlretrieve
'''

import urllib.request

url = 'http://www.baidu.com/'  # 注意加上/ 才是整的url

response = urllib.request.urlopen(url)  # 用urllib.request.urlopen(url) ，发送请求
# response 是个对象，包括5个方法:
# .read()    读取相应内容，只能读取byte类型
# .geturl()   获得url
# .getheaders() 获得头部信息
# .getcode()    获得状态码
# .readlines()  按行读取，返回一个list

print(response.read())  # 注意代码抓取是个二进制byte类型
print(response.read().decode())  # 查看编码类型，然后解码成字符串

# 把网页源代码，保存到文件夹
# 注意：with open 是如果没有对应的文件名，则新建一个文件
with open('baidu.html', 'wb') as fp:
    fp.write(response.read())









































