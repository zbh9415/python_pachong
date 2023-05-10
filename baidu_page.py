import requests
import re
import time
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}



def baidu(company,page):
    url = 'http://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word='+ company +str(page)
    res = requests.get(url, headers=headers).text

    block = re.findall('<h3 class="news-title_1YtI1 ">(.*?)</div></div>', res, re.S)

    title = []
    href = []
    date = []
    source = []


    for news in block:
        href.append(re.findall('<a href="(.*?)"', news, re.S))
        date.append(
            re.findall('<span class="c-color-gray2 c-font-normal c-gap-right-xsmall".*?>(.*?)</span>', news, re.S))
        source.append(re.findall('<span class="c-color-gray".*?>(.*?)</span>', news, re.S))
        title.append(re.findall('aria-label="标题：(.*?)"', news, re.S))

    date_bug = [[]]
    date2 = ['[无]' if x in date_bug else x for x in date]


    for i in range(10):
        # title[i] = title[i].strip()
        # title[i] = re.sub('<.*?>', '', title[i])
        x = int(page)
        print(str(x + i + 1) + ',' + str(title[i]), str(source[i]), str(date2[i]))
        print(href[i])

    file1 = open('D:\\数据挖掘信息.txt','a')
    file1.write(company + '数据挖掘完成！' + '\n' +'\n')
    for i in range(len(title)):
        x = int(page)
        file1.write(str(x + i + 1) + "," +str(title[i])+ '(' +str(date2[i])+'-' + str(source[i]) + ')' +'\n')
        file1.write(str(href[i]) +'\n')
    file1.write('----------------------'+'\n'+'\n')

companys = ['阿里巴巴','淘宝','京东','腾讯']

for com in companys:
    for i in range(5):
        baidu(com,str(i*10))
        print("成功")
        time.sleep(3)
