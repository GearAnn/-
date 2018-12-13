#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 模拟账户密码登录.py
@time: 2018/12/5 0005 下午 7:16
"""

"""
账户密码登录：本质上就是发一个POST,POST中包含了一张表单，表单里有账户密码。

目的：通过python来完成账户密码表单在发送。
"""
import urllib.request,urllib.parse

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20181131944714'

# 表单数据
form_data ={
'icode':'',
'key_id':'1',
'email':'494792590@qq.com',
'password':'bd6f116f8977f30ea639400191031d9aef2779c9560b729e84bb6ba54f2ae5c5',
'rkey':'fadff523aaff6e83227ac1509d88c752',
'f':'http%3A%2F%2Fwww.renren.com%2F284191275%2Fprofile',
'origURL':'	http://www.renren.com/home',
'domain':'renren.com',
'captcha_type':	'web_login',
}

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/70.0.3538.110 Safari/537.36'}

request = urllib.request.Request(url=post_url,headers=headers)

# 处理表单数据,urllib.parse.urlencode(form_data)只是把数据给拼接好，所以要加上encode()进行编码后发送
form_data = urllib.parse.urlencode(form_data).encode()

response = urllib.request.urlopen(request,data=form_data)
print(response.read().decode())
# 至此，就登录成功了






















