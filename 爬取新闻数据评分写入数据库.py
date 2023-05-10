import requests
import re
import time
import pymysql

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

def baidu(company):
    url = 'http://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word='+ company #+str(page)
    res = requests.get(url, headers=headers).text

    block = re.findall('<h3 class="news-title_1YtI1 ">(.*?)</div></div>', res, re.S)
    title = []
    href = []
    date = []
    source = []

    for news in block:
        href.append(re.findall('<a href="(.*?)"', news, re.S))
        date.append(re.findall('<span class="c-color-gray2 c-font-normal c-gap-right-xsmall".*?>(.*?)</span>', news, re.S))
        source.append(re.findall('<span class="c-color-gray".*?>(.*?)</span>', news, re.S))
        title.append(re.findall('aria-label="标题：(.*?)"', news, re.S))

    for i in range(len(date)):
        if date[i] == []:
            date[i]=[' ']

    for i in range(len(title)):
        #title[i] = title[i].strip() #取消两端的换行和空格，目前2020-10并没有换行所以不用
        title[i][0] = re.sub('<.*?>','',title[i][0])
    # print(title)
    #     date[i] = date[i].split(' ')[0]
    #     date[i] = re.sub('年','-',date[i])
    #     date[i] = re.sub('月', '-', date[i])
    #     date[i] = re.sub('日','-',date[i])
        if ('小时' in date[i][0]) or ('分钟' in date[i][0]):
            date[i][0] = time.strftime("%Y-%m-%d")
        else:
            date[i][0] = date[i][0]

    score = []
    keywords = ['违约','诉讼','兑付','阿里','京东','百度','互联网']
    for i in range(len(title)):
        num = 0
        try:
            artcle = requests.get(href[i][0],headers = headers).text
        except:
            article = '单个新闻爬取失败'

        try:
            artcle = artcle.encode('ISO-8859-1').decode('utf-8')
        except:
            try:
                artcle = artcle.encode('ISO-8859-1').decode('gbk')
            except:
                artcle = artcle
        p_artcle = '<p.*?>(.*?)</p>'
        artcle_main = re.findall(p_artcle,artcle,re.S)
        artcle = ''.join(artcle_main)
        for k in keywords:
            if (k in artcle) or (k in title[i][0]):
                num -= 5
        score.append(num)

    for i in range(len(title)):
        print(str(i + 1)+'.'+title[i][0]+'('+date[i][0]+' '+source[i][0]+')')
        print(href[i][0])
        print(company + "该新闻评分为"+str(score[i]))

    for i in range(len(title)):         #将内容写入数据库
        db = pymysql.connect(host='localhost', port=3306, user='root', database='pachong', charset='utf8')
        cur = db.cursor()

        sql_1 = 'SELECT * FROM test WHERE company = %s'
        cur.execute(sql_1,company)
        data_all = cur.fetchall()
        title_all = []
        for j in range(len(data_all)):
            title_all.append(data_all[j][1])
        if title[i] not in title_all:
            sql_2 = 'INSERT INTO test(company,title[i],href,source,date) VALUES (%s,%s,%s,%s,%s)'
            cur.execute(sql_2,(company,title[i],href[i],source[i],date[i]))
            db.commit()
        cur.close()
        db.close()
    print('--------------------------------------')

company=['阿里巴巴']
baidu(company)