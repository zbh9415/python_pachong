# =============================================================================
# 3.5.2 新浪财经数据挖掘实战 by 王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

import requests
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

def xinlang(company):
    url = 'https://search.sina.com.cn/?q=' + company + '&range=all&c=news&sort=time&ie=utf-8'
    res = requests.get(url, headers=headers, timeout=10).text
    # print(res)

    p_title = '<h2><a href=".*?" target="_blank">(.*?)</a>'
    p_href = '<h2><a href="(.*?)" target="_blank">'
    p_date = '<span class="fgray_time">(.*?)</span>'
    title = re.findall(p_title, res, re.S)  # 注意偶尔有的地方有换行，所以得加re.S（标题和链接其实不加也没事，主要是date得加）
    href = re.findall(p_href, res, re.S)  # 注意偶尔有的地方有换行，所以得加re.S（标题和链接其实不加也没事，主要是date得加）
    date = re.findall(p_date, res, re.S)  # 注意有的地方有换行，所以得加re.S，可以打印源代码后搜索fgray_time查看日期（更新）
    # print(title)
    # print(href)
    # print(date)

    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])
        date[i] = date[i].split(' ')[1]  # 获取来源的话，把[1]换成[0]就是来源了，如果有换行，通过strip()函数处理即可
        print(str(i + 1) + '.' + title[i] + ' - ' + date[i])
        print(href[i])

# xinlang('京东')  # 可以通过这个来调试


companys = ['阿里巴巴', '万科集团', '百度', '腾讯', '京东']
for i in companys:
    try:
        xinlang(i)
        print(i + '新浪财经新闻获取成功')
    except:
        print(i + '新浪财经新闻获取失败')

