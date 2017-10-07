import re

import pymysql
import requests
from bs4 import BeautifulSoup
from 爬虫.爬陈浩.fenlei_model import fenlei
def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='xcf232330',
        charset='utf8',
        use_unicode=False
    )
    return conn
dbObject = dbHandle()
cursor = dbObject.cursor()

def shengyu():
    sql = 'select * from pachong_test.kuke_copy'
    try:
        # date =datetime.now() + timedelta(hours=item['id'])
        cursor.execute(sql)
        # print(dbObject.commit())
        gong=cursor.fetchall()
        return gong
    except Exception as e:
        print(e)
        # print(item['title'] + '出现错误')
        dbObject.rollback()
gong = shengyu()

def delete_wuyong(model_div):
    try:
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
    except Exception as e:
        print(e)
    else:
        return model_div

# def save(model):
#     try:
#         model_text = requests.get(model.content).text
#         model_bs = BeautifulSoup(model_text, 'lxml')
#         model_div = model_bs.find_all('div', class_='entry-content')[0]
#         model_div = delete_wuyong(model_div)
#         prelist = model_div.find_all('pre')
#         for pre in prelist:
#             code = model_bs.new_tag('code')
#             code.string = pre.string
#             pre.clear()
#             pre.append(code)
#         if model_div.img:
#             model.fengmian = model_div.img['src']
#         model.content = str(model_div)
#         model.save_blog()
#     except Exception as e:
#         raise



def jianmo(url):
    try:
        url_text = requests.get(url).text
        url_bs = BeautifulSoup(url_text, 'lxml')
        print('         log:网页源码解析完毕')
        header = url_bs.find_all('header', class_='entry-header')[0]
        yuedu = int((re.split(r'[ ]*', header.h5.text)[-2:-1][0]).replace(",", ""))
        title = header.h1.text
        model = fenlei(title,yuedu,'')
        print('         log:正在解析内容')
        model_div = url_bs.find_all('div', class_='entry-content')[0]
        print('         log:正在过滤无用标签')
        model_div = delete_wuyong(model_div)
        prelist = model_div.find_all('pre')
        print('         log:正在进行代码格式化')
        for pre in prelist:
            if pre.string:
                code = url_bs.new_tag('code')
                code.string = pre.string
                pre.clear()
                pre.append(code)
        if model_div.img:
            model.fengmian = model_div.img['src']
        model.content = str(model_div)
        print('         log:正在保存')
        model.save_blog()
            # context_url = one.h2.a['href']
            # # context_url = 'https://coolshell.cn/articles/11466.html'
            # title = one.h2.a.string
            # yuedu = int((re.split(r'[ ]*', one.div.h5.text)[-2:-1][0]).replace(",", ""))
            # fl = fenlei(title, yuedu, context_url)
            # fl.url = context_url
            # save(fl)

    except Exception as e:
        print(e)
    pass
for url in gong:
    print('log:开始爬取'+str(url[2]))
    jianmo(url[2])