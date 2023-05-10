import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

url = 'https://search.sina.com.cn/?q='+'阿里巴巴'+'&c=news&from=channel&ie=utf-8'
res = requests.get(url, headers=headers).text

block = re.findall('<div class="r-info r-info2">(.*?)</div>', res, re.S)
title = []
href = []
time = []

# for news in block:
#     href.append(re.findall('<h2><a href=(.*?)" target', news, re.S))
#     time.append(re.findall('<h2>.*?fgray_time(.*?)</h2>', news, re.S))
# for i in range(len(time)):
#     time[i] = time[i].strip()
#     time[i] = re.sub('\t','',time[i])
# for i in range(len(time)):
#     time[i] = time[i].strip()
#     time[i] = re.sub('\n','',time[i])
# for i in range(len(time)):
#     time[i] = time[i].strip()
#     time[i] = re.sub(' ', '', time[i])
# for i in range(len(time)):
#     time[i] = time[i].strip()
#     time[i] = re.sub('">', '', time[i])
#     title.append(re.findall('<h2><a href=.*?blank">(.*?)</a>', news, re.S))

# print(news)


#标题的打印
p_href = re.findall('<h2><a href=(.*?)" target', res, re.S)
print(p_href)
p_title = re.findall('<h2><a href=.*?blank">(.*?)</a>', res, re.S)
for i in range(len(p_title)):
    p_title[i] = p_title[i].strip()
    p_title[i] = re.sub('<.*?>','',p_title[i])      #清洗数据，去除标题数据中的<>内容

print(p_title)

#公司时间来源的打印
p_time = re.findall('<h2>.*?fgray_time(.*?)</h2>', res, re.S)
# for i in range(len(p_time)):
#     p_time[i] = p_time[i].strip()
#     p_time[i] = re.sub('\t','',p_time[i])
# for i in range(len(p_time)):
#     p_time[i] = p_time[i].strip()
#     p_time[i] = re.sub('\n','',p_time[i])
# for i in range(len(p_time)):
#     p_time[i] = p_time[i].strip()
#     p_time[i] = re.sub(' ', '', p_time[i])
# for i in range(len(p_time)):
#     p_time[i] = p_time[i].strip()
#     p_time[i] = re.sub('">', '', p_time[i])
print(p_time)




