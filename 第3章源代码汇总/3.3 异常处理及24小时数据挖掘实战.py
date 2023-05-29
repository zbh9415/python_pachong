# =============================================================================
# 3.3 异常处理及24小时数据挖掘实战 by 王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================
import requests
import re
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


def baidu(company):
    url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=' + company
    res = requests.get(url, headers=headers).text
    # print(res)

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

    # print(1 + '1')


# companys = ['华能信托', '阿里巴巴', '万科集团', '百度集团', '腾讯', '京东']
# for i in companys:
#     baidu(i)
#     print(i + '百度新闻爬取成功')

# companys = ['华能信托', '阿里巴巴', '万科集团', '百度集团', '腾讯', '京东']
# for i in companys:
#     try:
#         baidu(i)
#         print(i + '百度新闻爬取成功')
#     except:
#         print('爬取有问题，接着爬下一家公司')

while True:  # 一直运行的意思
    companys = ['华能信托', '阿里巴巴', '万科集团', '百度集团', '腾讯', '京东']
    for i in companys:
        try:
            baidu(i)
            print(i + '百度新闻爬取成功')
        except:
            print(i + '百度新闻爬取失败')

    time.sleep(3600)  # 每3600秒运行一次，即3小时运行一次，注意缩进
