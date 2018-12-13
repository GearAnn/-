#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 爬百度贴吧.py
@time: 2018/11/26 0026 下午 7:24
"""
"""
目的：
爬取百度贴吧信息，输入吧名，输入起始页码，
然后在当前文件夹中创建一个文件夹，文件夹里面是贴吧每一页的HTML。
"""

import urllib.parse,urllib.request

# EVE游戏贴吧url，抹去了第一页最后的pn=0
url = 'https://tieba.baidu.com/f?kw=eve%E6%AC%A7%E6%9C%8D&ie=utf-8&'
# 从url规律中可以发现贴吧第一页pn==0,第二页pn==50，表示页码page==(n-1)*50

ba_name = input('输入要爬取的吧名：')
start_page = int(input('输入要爬取的起始页码：'))
end_page = int(input('输入要爬取的结束页码：'))

# 创建贴吧html文件夹,引入os模块
import os
if not os.path.exists(ba_name):  # if not:如果条件xx的结果不为真
    # 如果不进行isExists的判断的话文件夹重名的话会报错
    os.mkdir(ba_name)
    # 注意：所以如果文件夹名字存在,os.path.exists(ba_name)为真，则if not下面的代码不执行

# 利用循环，依次爬取每一页
for page in range(start_page, end_page+1):  # 注意：range区间的属性要加+1
    # page是当前页，拼接url
    data = {
        'kw': ba_name,
        'pn': (page-1)*50

    }
    data = urllib.parse.urlencode(data)
    url_new = url + data

    # 定制请求头
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/63.0.3239.26Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2767.400', }
    # 创建请求对象
    request = urllib.request.Request(url=url_new, headers=headers)
    print('第%s页开始下载...' % page)
    response = urllib.request.urlopen(request)

    # 在html文件中生成贴吧页码
    html_name = ba_name + '_' + str(page) + '.html'
    # 拼接文件路径,把爬取到的html放在贴吧文件夹中
    html_path = ba_name + '/' + html_name
    # 写内容
    with open(html_path, 'wb') as fp:  # 保存响应
        fp.write(response.read())

    print('第%s页结束下载...' % page)

















