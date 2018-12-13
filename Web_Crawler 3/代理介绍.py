#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 代理介绍.py
@time: 2018/12/4 0004 上午 11:24
"""

"""
代理介绍
正向代理：代理客户端获取数据；
方向代理：代理服务器提供数据;

透明代理：对方服务器可以识别你使用了代理，也可获取你的真实IP;
匿名代理：对方服务器可以识别你使用了代理，但无法获取你的真实IP；
高匿名代理：对方服务器无法识别你使用了代理，也无法获取你的真实IP。

代理网站：西刺代理，花刺代理验证(用于验证IP和端口是否可用)
设置代理步奏：
1.打开浏览器设置 - 工具 - Internet选项
2.连接 - 局域网设置 - 代理服务器中
3.输入：代理网站上的IP地址和端口号


目的：使用一个代理来发送请求。
"""
import urllib.request,urllib.parse

# 代理代理网站上找一个代理IP和端口 113.79.75.104：9797
# 创建handler
handler = urllib.request.ProxyHandler({'http': '113.79.75.104：9797'})

# 创建opener
opener = urllib.request.build_opener(handler)

url = 'http://www.baidu.com/s?ie=utf-8&wd=ip'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/63.0.3239.26Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3'}

# 构建请求
request = urllib.request.Request(url=url, headers=headers)

# 发送请求
response = opener.open(request)

# 保存响应信息
with open('ip.html', 'wb') as fp:
    fp.write(response.read())

# 注意：若运行报错则 代理的IP和端口不能用，需要换一个。














