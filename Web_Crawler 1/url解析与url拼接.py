#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: url解析.py
@time: 2018/11/25 0025 上午 4:32
"""
import urllib.parse

# 因为url只能由特定字符组成，如：字母、数字、下划线
# 如果出现其他字符，如：空格、中文 等，就需要对其他字符编码(编成16进制),利用 urllib.parse

# urllib.parse.quote()   编码：编成电脑看的字符，把url中的其他字符换成16进制byte类型
# urllib.parse.unquote()   解码：解成人看的字符，把url中的16进制换成汉字等字符
# urlib.parse.urlencode()  将字典拼接成query_string

url = 'http://www.baidu.com/index.html?name=安安&pwd=123456'

# 把url其他字符编为16进制，才可读
ret = urllib.parse.quote(url)
print(ret)
# 返回：http%3A//www.baidu.com/index.html%3Fname%3D%E5%AE%89%E5%AE%89%26pwd%3D123456


# 对url进行字符串拼接
url1 = 'http://www.baidu.com/index.html'

# 参数类型是单个，如何拼接
name = 'ann'
age = 16
# 参数是字典，如何拼接
data = {'heigh': 170, 'gender': 'man'}

# urllib.parse.urlencode() ：就是把字典给自动拼接好
query_string = urllib.parse.urlencode(data)
print(query_string)  # 返回： heigh=170&gender=man



# 下面是自己写的类似 urlbli.parse.urlencode() 的函数:
# list = []
# for i, j in data.items():  # 注意：i是键 ，j是值 , item方法把字典转换为元组,才可以用for 同时取2个元素
#     list.append(i + '=' + str(j))  # 把键值对用 = 进行拼接，还要把int转为str
#     # 拼接完成后，装入空列表
# query_string = '&'.join(list)
#
# url1 = url1 + '?' + query_string
#
# print(url1)






























