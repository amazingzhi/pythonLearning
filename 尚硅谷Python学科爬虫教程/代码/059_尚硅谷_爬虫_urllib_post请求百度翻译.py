

# post请求: 向server传入数据
# 这个章节解决的是，当你向网页中传输了数据之后，页面发生了改变的情况下，然后再下载页面的问题。

import urllib.request
import urllib.parse

# 找接口：在翻译网页中右键inspect，找到Network里哪个真正实现了翻译，用它的request url
url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

data = {
    'kw':'spider'
}

# post请求的参数 必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')  # post请求的参数 必须要进行编码

# post的请求的参数 是不会拼接在url的后面的  而是需要放在请求对象定制的参数中
request = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')
print(content)
# 字符串--》json对象

import json

obj = json.loads(content)
print(obj)



# post请求方式的参数 必须编码   data = urllib.parse.urlencode(data)
# 编码之后 必须调用encode方法 data = urllib.parse.urlencode(data).encode('utf-8')
# 参数是放在请求对象定制的方法中  request = urllib.request.Request(url=url,data=data,headers=headers)

