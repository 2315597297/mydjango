# from bs4 import BeautifulSoup
#
# s='''
# <pre><code>&gt;&gt;&gt; name = input()
# Michael
# </code></pre>
# '''
# ss=s.replace(' ', "&nbsp;").replace("\n", r"<br/>").replace("\r", "<br/>")
# sss=BeautifulSoup(ss,'lxml')
# print(sss)
# list  =['s','b','q','c']
# print(list[2:])
# from 爬虫.爬廖雪峰老师.fenlei_model import fenlei
#
# b = fenlei('ceshi','sadfasdfsdafsdfsdafsad')
# b.save_blog()

# start_urls = ['https://coolshell.cn/page/'+str(page) for page in range(1,5) ]
# print(start_urls)
# i='img/bd_logo1.png'
#
# if 'https://' in  i or 'http://'in i:
#     print('外链')
import json
key = '是一种最常见的二进制编码方法'
key_list = list(key)
print(key_list[1:])
print(key_list)
key_ =[]
# print(key_list[0,1])

for i in range(1,key_list.__len__()):
    for index,a in enumerate(key_list[:-i]):
        value = a + ''.join(key_list[index + 1:index + 1 + i])
        print(value)
        key_.append(value)

print(len(key_list))
print(len(key_))

# key_2= [a+b for index,a in enumerate(key_list[:-2]) for b in key_list[index,index+2]]
# print(key_2)
