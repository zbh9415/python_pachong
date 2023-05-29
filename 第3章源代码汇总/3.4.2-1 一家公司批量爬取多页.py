# =============================================================================
# 3.4.2-1 一家公司批量爬取多页 by 王宇韬  代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

import requests
import re
import time
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

# 爬取一个公司的多页
def baidu(page):
    num = (page - 1) * 10  # 参数规律是（页数-1）*10
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=阿里巴巴&pn=' + str(num)
    res = requests.get(url, headers=headers).text
    # 其他相关爬虫代码

    p_href = '<h3 class="news-title_1YtI1"><a href="(.*?)"'
    href = re.findall(p_href, res, re.S)
    p_title = '<h3 class="news-title_1YtI1">.*?>(.*?)</a>'
    title = re.findall(p_title, res, re.S)
    p_date = '<span class="c-color-gray2 c-font-normal">(.*?)</span>'
    date = re.findall(p_date, res)
    p_source = '<span class="c-color-gray c-font-normal c-gap-right">(.*?)</span>'
    source = re.findall(p_source, res)

    for i in range(len(title)):  # range(len(title)),这里因为知道len(title) = 10，所以也可以写成for i in range(10)
        title[i] = title[i].strip()  # strip()函数用来取消字符串两端的换行或者空格，不过这里好像不太需要了
        title[i] = re.sub('<.*?>', '', title[i])  # 核心，用re.sub()函数来替换不重要的内容
        print(str(i + 1) + '.' + title[i] + '(' + date[i] + '-' + source[i] + ')')
        print(href[i])


for i in range(10):  # 这里一共爬取了10页
    baidu(i+1)  # i是从0开始的序号，所以要写成i+1表示第几页
    print('第' + str(i+1) + '页爬取成功')  # i是从0开始的序号，所以写i+1
    time.sleep(3)  # 不要爬太快，爬太快会被百度反爬

