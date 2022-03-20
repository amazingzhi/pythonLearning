

import urllib.request

url = 'https://www.baidu.com'  # 如果出现下载数据过少，可能是遭遇了反爬虫手段， UA反扒，他识别不了你是真正的浏览器，所以需要加上自己的User Agent。

# url的组成
# https://www.baidu.com/s?wd=周杰伦

# http/https    www.baidu.com   80/443     s      wd = 周杰伦                  #
#    协议             主机        端口号     路径     参数（问号后的数据）           锚点
# http   80
# https  443
# mysql  3306
# oracle 1521
# redis  6379
# mongodb 27017

# 找到自己的UA：随便找一个网页，右键inspect，在network栏里找到headers，如果没有，刷新页面，在headers的最后一行就是UA
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

# 因为urlopen方法中不能存储字典 所以headers不能传递进去
# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')

print(content)

