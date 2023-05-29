# =============================================================================
# 3.5.1 搜狐新闻数据挖掘实战 by 王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

url = 'https://www.sogou.com/sogou?ie=utf8&interation=1728053249&interV=&&query=阿里巴巴'
res = requests.get(url, headers=headers, timeout=10).text
# print(res)

p_source = '<p class="news-from text-lightgray">.*?<span>(.*?)</span><span>.*?</span>.*?</p>'
source = re.findall(p_source, res, re.S)
# print(source)

p_date = '<p class="news-from text-lightgray">.*?<span>.*?</span><span>(.*?)</span>.*?</p>'
date = re.findall(p_date, res, re.S)
# print(date)

p_title = '<h3 class="vr-title">.*?<a id=".*?" target="_blank"  cacheStrategy="qcr:-1" href=".*?">(.*?)</a>'
title = re.findall(p_title, res, re.S)  # 因为正则里<h3 class="vr-title">后有换行，所以得加re.S
# print(title)

p_href = '<h3 class="vr-title">.*?<a id=".*?" target="_blank"  cacheStrategy="qcr:-1" href="(.*?)">.*?</a>'
href = re.findall(p_href, res, re.S)  # 因为正则里<h3 class="vr-title">后有换行，所以得加re.S
# print(href)

print(title)

for i in range(len(title)):
    title[i] = re.sub('<.*?>', '', title[i])
    href[i] = 'https://www.sogou.com' + href[i]
    print(str(i+1) + '.' + title[i] + '-' + date[i] + '-' + source[i])
    print(href[i])
