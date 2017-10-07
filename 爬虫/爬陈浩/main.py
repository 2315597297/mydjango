# import random
# from time import sleep
#
# import requests
# from bs4 import BeautifulSoup, Tag
#
# from 爬虫.爬廖雪峰老师.fenlei_model import fenlei
# weburl='https://www.liaoxuefeng.com'
#
# #----------------------------用于获取博客的内容
# def getcontext(url):
#     context=BeautifulSoup(requests.get(url).text,'lxml')
#     context_tag=context.find('div',class_='x-wiki-content x-main-content')
#     # 用于内容中img标签中的src路径是相对路径  我们需要将其修改为连接到廖老师网址的绝对路径
#     if context_tag:
#         img_list=context_tag.find_all('img')
#         for img in img_list:
#             img['src']=weburl+img['src']
#     return str(context_tag)
#
# #得到目录list
# def getMLlist():
#     requests_text = requests.get('https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000').text
#     bs = BeautifulSoup(requests_text, 'html5lib')
#     return bs.find_all('ul', class_='uk-nav uk-nav-side', style='margin-right:-15px;')
#
#
# mulu_list = getMLlist()
#
# mulu_tag =None
# if mulu_list:
#     mulu_tag=mulu_list[0]
# else:
#     #抛出异常  程序停止
#     pass
#
# count =1
# for fl in mulu_tag.find_all('a'):
#     f=fenlei('第'+count.__str__()+'节_'+fl.string,getcontext(weburl+fl['href']))
#     # sleep(random.randint(1,2))
#     while f.save_blog():
#         f = fenlei('第' + count.__str__() + '节_' + fl.string, getcontext(weburl + fl['href']))
#     count+=1
#
#
#
#
# #".replaceAll(" ","&nbsp;").replaceAll("\r","<br/>");
#
# #出现问题的
# #python基础_第104篇_async/await
# #python基础_第85篇_TCP/IP简介
# #python基础_第29篇_map/reduce
import re
import requests
from bs4 import BeautifulSoup
from 爬虫.爬陈浩.fenlei_model import fenlei

web_url='https://coolshell.cn/'

url_list = [web_url+'/page/'+str(a) for a in range(1,71)]
def delete_wuyong(model_div):
    if model_div.find('div', id='wp_rp_first'):
        model_div.find('div', id='wp_rp_first').decompose()
    if model_div.find('div', class_='post-ratings'):
        model_div.find('div', class_='post-ratings').decompose()
    if model_div.find('div', class_='jiathis_style'):
        model_div.find('div', class_='jiathis_style').decompose()
    if model_div.find('div', class_='post-ratings-loading'):
        model_div.find('div', class_='post-ratings-loading').decompose()
    if model_div.find('div', class_='post-ratings-image'):
        model_div.find('div', class_='post-ratings-image').decompose()


    return model_div

def save(model):
    try:
        model_text = requests.get(model.content).text
        model_bs = BeautifulSoup(model_text, 'lxml')
        model_div = model_bs.find_all('div', class_='entry-content')[0]
        model_div = delete_wuyong(model_div)
        prelist = model_div.find_all('pre')
        for pre in prelist:
            code = model_bs.new_tag('code')
            code.string = pre.string
            pre.clear()
            pre.append(code)
        if model_div.img:
            model.fengmian = model_div.img['src']
        model.content = str(model_div)
        model.save_blog()
    except Exception as e:
        raise



def jianmo(url):
    try:
        url_text = requests.get(url).text
        url_bs = BeautifulSoup(url_text, 'lxml')
        mulu_list = url_bs.find_all('header', class_='entry-header')
        context_url = ''
        for one in mulu_list:
            context_url = one.h2.a['href']
            # context_url = 'https://coolshell.cn/articles/11466.html'
            title = one.h2.a.string
            yuedu = int((re.split(r'[ ]*', one.div.h5.text)[-2:-1][0]).replace(",", ""))
            fl = fenlei(title, yuedu, context_url)
            fl.url = context_url
            save(fl)

    except Exception as e:
        print('出现异常！url='+context_url,end='')
        print(e)

    # fenlei = fenlei_model()
    pass
for url in url_list:
    jianmo(url)