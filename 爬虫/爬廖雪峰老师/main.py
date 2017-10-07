import random
from time import sleep

import requests
from bs4 import BeautifulSoup, Tag

from 爬虫.爬廖雪峰老师.fenlei_model import fenlei
weburl='https://www.liaoxuefeng.com'

#----------------------------用于获取博客的内容
def getcontext(url):
    context=BeautifulSoup(requests.get(url).text,'lxml')
    context_tag=context.find('div',class_='x-wiki-content x-main-content')
    # 用于内容中img标签中的src路径是相对路径  我们需要将其修改为连接到廖老师网址的绝对路径
    if context_tag:
        img_list=context_tag.find_all('img')
        for img in img_list:
            img['src']=weburl+img['src']
    return str(context_tag)

#得到目录list
def getMLlist():
    requests_text = requests.get('https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000').text
    bs = BeautifulSoup(requests_text, 'html5lib')
    return bs.find_all('ul', class_='uk-nav uk-nav-side', style='margin-right:-15px;')


mulu_list = getMLlist()

mulu_tag =None
if mulu_list:
    mulu_tag=mulu_list[0]
else:
    #抛出异常  程序停止
    pass

count =1
for fl in mulu_tag.find_all('a'):
    f=fenlei('第'+count.__str__()+'节_'+fl.string,getcontext(weburl+fl['href']))
    # sleep(random.randint(1,2))
    while f.save_blog():
        f = fenlei('第' + count.__str__() + '节_' + fl.string, getcontext(weburl + fl['href']))
    count+=1




#".replaceAll(" ","&nbsp;").replaceAll("\r","<br/>");

#出现问题的
#python基础_第104篇_async/await
#python基础_第85篇_TCP/IP简介
#python基础_第29篇_map/reduce
