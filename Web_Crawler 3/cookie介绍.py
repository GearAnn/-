#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: cookie介绍.py
@time: 2018/12/4 0004 上午 11:45
"""

"""
cookie:浏览器缓存,指某些网站为了辨别用户身份、进行 session 跟踪而储存在用户本地终端上的数据（通常经过加密）,最新取代的规范是 RFC6265
       简单来说,Cookie就是个人信息标签。

目的：模拟一个cookie来发送请求,直接通过保存在html进入网站账户登录后的页面
注意：POST中没有set-Cookie

步奏；
1、登录‘人人网’；
2、登录一个空白账号；
3、点击个人网页，就会抓到发送的html文档请求，里面就有Cookie

注意：想清楚为什么在登录账户的请求中抓不到Cookie,必须在登录后的个人网页中才能抓到需要的Cookie?
     因为，在登录个人网页的时候，会发送新的request,新的request就会包含个人的Cookie，也就是个人身份标签。

"""
import urllib.request
import urllib.parse

url = 'http://www.renren.com/960481378/profile'  # 960481378是人人网账户，个人可以重新建立一个新的空账户

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/63.0.3239.26Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3',

    'Cookie': 'anonymid=jp97wcnq-ww9vq3; depovince=CQ; _r01_=1; JSESSIONID=abcLZQuCcXuUc9nImf_Dw; \
    ick_login=df1279d1-4254-42ed-adf5-a34f335c6d3a; first_login_flag=1; ln_uact=494792590@qq.com; ln_hurl=\
    http://hdn.xnimg.cn/photos/hdn421/20110614/2335/main_jBdw_221460p019118.jpg; loginfrom=syshome; ch_id=10016; \
    jebe_key=e321665a-52d6-49de-989a-a4e8f8bbee5b%7Cd56b85b15b392f57c5160294f9c94c76%7C1544008561806%7C1%7C154400838969\
    4; wp_fold=0; wp=0; jebecookies=6ae7eafd-8fe6-4000-ab15-fd9d1f673f32|||||; _de=06BE46C99C9B11E8530F97F46C27D779696B\
    F75400CE19CC; p=9cf72c062b61fb84179a9be2b47a91775; t=09761a9787c2e00a60f14f4b77e774225; societyguester=09761a9787c2\
    e00a60f14f4b77e774225; id=284191275; xnsid=81e3a955'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

with open('renren.html', 'wb') as fp:
    fp.write(response.read())

# 注意：很多时候就算你粘贴了Cookie还是无法登录，这个时候你就需要把所有的头部信息全部粘贴才可以登录。
