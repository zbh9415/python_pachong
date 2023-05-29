# =============================================================================
# 1.2.4 运算符介绍与实践 by 华能信托-王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

# 1 算术运算符：+ 、-、*、/
a = 'hello'
b = 'world'
c = a + ' ' + b
print(c)

# 2 比较运算符： > , <, ==
score = -10
if score < 0:
    print('该新闻是负面新闻，录入数据库')

a = 1
b = 2
if a == b:  # 注意这边是两个等号
    print('a和b相等')
else:
    print('a和b不相等')

# 3 逻辑运算符：not，and，or
score = -10
year = 2018
if (score < 0) and (year == 2018):
    print('录入数据库')
else:
    print('不录入数据库')

