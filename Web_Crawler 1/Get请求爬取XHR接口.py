#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 爬取豆瓣电影.py
@time: 2018/11/26 0026 上午 6:48
"""
"""
目的：利用Ajax接口(get方式), 抓取豆瓣上的电影,Ajax返回的一般是Json类型的数据。
"""

import urllib.parse,urllib.request

# 初始url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend\
# &page_limit=20&page_start=0'

# 分析输出的url发现'&page_limit=20&page_start=0',就是第一页显示20个数据(电影),所以可以对初始url进行修改
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&'

# page转成数字类型，后面作加法
page = int(input('输入想要第几页的数据：'))

number = 20  # 一页显示20条数据(电影)
# 构造get参数
data = {
    'page_start': (page-1)*number,   # 注意：page要转成数字才能做加法,page-1 是因为初始url的pagt_start是从0开始d的
    'page_limit': number,
}

# 将字典转为quert_string
query_string = urllib.parse.urlencode(data)
# 修改 url
url += query_string
# 构造头部
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26\
 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2767.400', }
# 构造请求对象
request = urllib.request.Request(url=url, headers=headers)
# 发送请求，获取响应
response = urllib.request.urlopen(request)

print(response.read().decode())
# 这样打印出来的就是任意页码的20条电影数据







