


import requests
#
'''
爬虫：就是请求网站并提取数据的自动化程序（自动化就是可以避开六浏览器）
爬虫能抓的数据形式：
Day12.网页文本：html文档,json格式文本
2.图片：获取到的时二进制文件，保持为图片格式


基本语法
requests.request()  # 构造一个请求，支持以下方法的基础方法
requests.get()   #  获取html网页的主要方法，对应于http的get
requests.head()  #  获取html网页的头部信息，对应于http的head
requests.post()  #  向html网页提交post请求，对应于http的post
requests.put()   #  向html网页提交put请求，对应于http的put
requests.patch()  #  向html网页提交局部修改请求，对应于http的patch
requests.delete()  #  向html网页提交删除请求,对应于http的delete

Post请求:是需要构建一个登录框才可以获取信息,而且url中不包含参数信息,post的请求头是form data的形式
Get请求:是把参数信息放在url里面

Requst包含4个内容：
Day12.请求方式主要有：get,post两种，还有hed,put,delete,options等
2.请求url：URL全称为统一资源定位符,网页文档，图片，视频都可以用URL来定位确定
3.请求头(request header):请求时的头部信息，如 User-agent, Host, Cookies 等信息
                        通过请求头，向服务器发送配置信息,服务器就可以判断你的浏览器,你的文档类型
4.请求体：请求时额外携带的数据，如表单提交的表单数据(比如网页登陆器的信息).


Response包含的内容：
Day12.状态码、状态响应(Status code)：200表示成功，301表示跳转，404表示找不到页面，502表示服务器错误
2.响应头:如内容长度，内容类型，服务器信息,Cookie
3.响应体（最重要的部分）：包含 请求资源的内容，网页HTML(网页源代码)，图片，二进制等数据


爬虫流程：
Day12.发起请求：向http发送一个request,请求还可以包含headers等信息
2.获取响应的内容:得到一个response内容，就是页面的内容，类型可能是HTML,Json字符串，二进制数据（如图片视频）
3.解析内容：得到的可能是html，那就直接用网页解析库或者正则表达式进行解析
            得到的是Json，就直接转Json对象解析
            得到的是二进制数据，可以保持或者进行其他处理
4.保存数据(DBA)：可以为文本，字典等类型 保存至数据库SQL

'''
# 获得一个网页
# r = requests.get('url')
# 构造一个向服务器请求资源的对象(request),返回服务器资源的（response）对象

response = requests.get('http://www.baidu.com')
# 拿到 response 中的3个内容
print(response.text)     # 获取了网页的源代码（html） 也就是响应体
print(response.status_code)  # 获取了服务器状态 200正常 响应状态码
print(response.headers)     # 获取了响应头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.Day12; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/65.0.3325.181 Safari/537.36'}  # 获取了请求头
# 下面的就是抓取源代码和头部信息
response = requests.get('http://www.baidu.com', headers=headers)
print(response.status_code)

# 抓取图片文件
response = requests.get('https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpo\
WK1HF6hhy/it/u=1331304461,1483529290&fm=27&gp=0.jpg')
print(response.content)  # coentent就是获取的响应题的二进制格式



