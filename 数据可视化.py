import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from scipy.stats import pearsonr


plt.rcParams["font.family"]="SimHei"

data=pd.read_excel('C:\\Users\\Administrator\\Desktop\\data.xlsx')
d = []
for i in range(len(data)):
    d.append(datetime.datetime.strptime(data['date'][i],'%Y-%m-%d'))
data['data']=d


plt.plot(data['date'],data['score'],"--",label = "评分")
plt.xticks(rotation = 45)
plt.legend(loc = 'upper left')
plt.twinx()
plt.plot(data['date'],data['price'],"r",label = "价格")
plt.xticks(rotation = 45)
plt.legend(loc = 'upper right')

corr=pearsonr(data['score'],data['price'])
print('相关性系数r值为'+str(corr[0])+',显著性水平p值'+str(corr[1]))
a='相关性系数r值为'+str(corr[0])+',显著性水平p值'+str(corr[1])
plt.title(a)

plt.show()