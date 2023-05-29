# =============================================================================
# 3.1 百度新闻数据挖掘 by 王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=阿里巴巴'  # 把链接中rtt参数换成4即是按时间排序，默认为1按焦点排序，3.4.1小节也有讲到
res = requests.get(url, headers=headers).text  # 加上headers用来告诉网站这是通过一个浏览器进行的访问
# print(res)

p_href = '<h3 class="news-title_1YtI1"><a href="(.*?)"'
href = re.findall(p_href, res, re.S)
p_title = '<h3 class="news-title_1YtI1">.*?>(.*?)</a>'
title = re.findall(p_title, res, re.S)
p_date = '<span class="c-color-gray2 c-font-normal">(.*?)</span>'
date = re.findall(p_date, res)
p_source = '<span class="c-color-gray c-font-normal c-gap-right">(.*?)</span>'
source = re.findall(p_source, res)

# print(title)
# print(href)
# print(date)
# print(source)

for i in range(len(title)):  # range(len(title)),这里因为知道len(title) = 10，所以也可以写成for i in range(10)
    title[i] = title[i].strip()  # strip()函数用来取消字符串两端的换行或者空格，不过目前（2020-10）并没有换行或空格，所以其实不写这一行也没事
    title[i] = re.sub('<.*?>', '', title[i])  # 核心，用re.sub()函数来替换不重要的内容
    print(str(i + 1) + '.' + title[i] + '(' + source[i] + ' ' + date[i] + ')')
    print(href[i])

