import requests
import re
import pymysql
company = '阿里巴巴'
with open("F:/mycode/file/sougou.txt", "r", encoding="GBK") as f:       #打开文本sougou的源代码
    url = f.read()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

# def baidu(company,page):
#     url = 'http://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word='+ company +str(page)
#     res = requests.get(url, headers=headers).text
block = re.findall('<div class="vrwrap"(.*?)<p class="star-wiki"', url, re.S)

title = []
href = []
date1 = []
source = []

for news in block:
    href.append(re.findall('<h3 class="vr-title">.*?href="(.*?)"', news, re.S))
    date1.append(re.findall('<p class="news-from text-lightgray">.*?</span><span>(.*?)</span>', news, re.S))
    source.append(re.findall('<p class="news-from text-lightgray">.*?<span>(.*?)</span>', news, re.S))
    title.append(re.findall('<h3 class="vr-title">.*?>(.*?)</a>', news, re.S))


for i in range(len(title)):
    title[i] = str(title[i]).strip()
    title[i] = re.sub("<!--red_beg-->",'',title[i])
for i in range(len(title)):
    title[i] = str(title[i]).strip()
    title[i] = re.sub('</em>','',title[i])
for i in range(len(title)):
    title[i] = str(title[i]).strip()
    title[i] = re.sub('<!--red_end-->', '', title[i])
for i in range(len(title)):
    title[i] = str(title[i]).strip()
    title[i] = re.sub('<em>', '', title[i])
for i in range(len(title)):
    title[i] = str(title[i]).strip()
    title[i] = re.sub("'",'',title[i])

date_bug = [[]]
date = ['[无]' if x in date_bug else x for x in date1]
# print(title)
# print(date)
# print(source)
# print(href)

for i in range(len(title)):
    db = pymysql.connect(host='localhost', port=3306, user='root', database='pachong', charset='utf8')
    cur = db.cursor()
    sql = 'INSERT INTO test(company,title,href,date,source) VALUES (%s,%s,%s,%s,%s)'
    cur.execute(sql,(company,title[i],href[i],date[i],source[i]))
    db.commit()
    cur.close()
    db.close()
