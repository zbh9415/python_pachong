# =============================================================================
# 2.4.5 正则表达式之小知识点补充 by 王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

# 1 re.sub()方法实现批量替换
# 1.1 传统方法-replace()函数
title = ['<em>阿里巴巴</em>代码竞赛现全球首位AI评委 能为代码质量打分']
title[0] = title[0].replace('<em>','')
title[0] = title[0].replace('</em>','')
print(title[0])

# 1.2 re.sub()方法
import re
title = ['<em>阿里巴巴</em>代码竞赛现全球首位AI评委 能为代码质量打分']
title[0] = re.sub('<.*?>', '', title[0])
print(title[0])

# 2 中括号[ ]的用法：使在中括号里的内容不再有特殊含义
company = '*华能信托'
company1 = re.sub('[*]', '', company)
print(company1)


