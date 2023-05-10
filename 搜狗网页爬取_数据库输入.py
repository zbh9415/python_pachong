import requests
import re
import pymysql
import time
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

def sougou(company,page):

    url = 'https://www.sogou.com/sogou?interation=1728053249&interV=&pid=sogou-wsse-8f646834ef1adefa&query=' + company + '&page='+ str(page)
    res = requests.get(url, headers=headers).text
    block = re.findall('<div class="vrwrap"(.*?)<p class="star-wiki"', res, re.S)

    title = []
    href = []
    date1 = []
    source = []

    for news in block:
        href.append(re.findall('<h3 class="vr-title">.*?href="(.*?)"', news, re.S))
        date1.append(re.findall('<p class="news-from text-lightgray">.*?</span><span>(.*?)</span>', news, re.S))
        source.append(re.findall('<p class="news-from text-lightgray">.*?<span>(.*?)</span>', news, re.S))
        title.append(re.findall('<h3 class="vr-title">.*?>(.*?)</a>', news, re.S))


    date_bug = [[]]         #数据清洗，如果日期不存在，将不存在的【】替换成【无】
    date = ['[无]' if x in date_bug else x for x in date1]


    for i in range(len(title)):             #数据清洗，去除标题中多余的东西
        title[i] = str(title[i]).strip()
        title[i] = re.sub("<!--red_beg-->", '', title[i])
    for i in range(len(title)):
        title[i] = str(title[i]).strip()
        title[i] = re.sub('</em>', '', title[i])
    for i in range(len(title)):
        title[i] = str(title[i]).strip()
        title[i] = re.sub('<!--red_end-->', '', title[i])
    for i in range(len(title)):
        title[i] = str(title[i]).strip()
        title[i] = re.sub('<em>', '', title[i])
    for i in range(len(title)):
        title[i] = str(title[i]).strip()
        title[i] = re.sub("'", '', title[i])

    print(title)
    print(date)
    print(source)
    print(href)
    print(company)

    # for i in range(len(title)):         #将内容写入数据库
    #     db = pymysql.connect(host='localhost', port=3306, user='root', database='pachong', charset='utf8')
    #     cur = db.cursor()
    #     sql = 'INSERT INTO test(company,title,href,date,source) VALUES (%s,%s,%s,%s,%s)'
    #     cur.execute(sql,(company,title[i],href[i],date[i],source[i]))
    #     db.commit()
    #     cur.close()
    #     db.close()


    # for i in range(10):           #打印模块
    #     # title[i] = title[i].strip()
    #     # title[i] = re.sub('<.*?>', '', title[i])
    #     x = int(page)
    #     print(str(x + i + 1) + ',' + str(title1[i]), str(source1[i]), str(date2[i]))
    #     print(href1[i])

    # file1 = open('D:\\数据挖掘信息.txt','a')        #写入模块，将数据写入到记事本中
    # file1.write(company + '数据挖掘完成！' + '\n' +'\n')
    # for i in range(len(title)):
    #     x = int(page)
    #     file1.write(str(x + i + 1) + "," +str(title[i])+ '(' +str(date2[i])+'-' + str(source[i]) + ')' +'\n')
    #     file1.write(str(href[i]) +'\n')
    # file1.write('----------------------'+'\n'+'\n')
#
# sougou('阿里巴巴',1)
companys = ['阿里巴巴','淘宝','京东','腾讯']
for com in companys:            #循环，多公司多页运行
    for i in range(len(companys)):
        p = i + 1
        sougou(com,p)
        print(com +str(p)+ "成功")
        time.sleep(10)
