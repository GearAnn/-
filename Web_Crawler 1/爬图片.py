#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 爬图片.py
@time: 2018/11/25 0025 上午 4:12
"""
import urllib.request

# 抓图片并保存的第一种方式：

# 网页上找到一个图片，右键复制图片地址，粘贴到下面
image_url = 'http://preview.quanjing.com/ph037/ph1466-p00383.jpg'

# 注意：图片抓取过来是以字符串的形式，然后我们需要把图片以byte读取，然后写入文件保存
response = urllib.request.urlopen(image_url)

# 图片只能以二进制的格式写入本地保存,因为爬取对象就是byte类型，所以直接写
with open('haidao.jpg', 'wb') as pc:
    pc.write(response.read())



# 第二种方式: 用 urlretrieve

# 2个参数：第一个是图片的url对象，第二个是图片保存的名字
urllib.request.urlretrieve(image_url, 'haidao2.jpg')







