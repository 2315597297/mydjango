import requests
from bs4 import BeautifulSoup
import pymysql


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
def save(item):
    sql = 'insert into pachong_test.kuke(title,url) values (%s,%s)'
    try:
        # date =datetime.now() + timedelta(hours=item['id'])
        cursor.execute(sql, (item['title'], item['url']))
        dbObject.commit()
    except Exception as e:
        print(e)
        print(item['title'] + '出现错误')
        dbObject.rollback()


web_url='https://coolshell.cn/'

url_list = [web_url+'/page/'+str(a) for a in range(1,71)]
def jianmo(url):
    url_text = requests.get(url).text
    url_bs = BeautifulSoup(url_text, 'lxml')
    mulu_list = url_bs.find_all('header', class_='entry-header')
    for one in mulu_list:
        d = {}
        d['title']=one.h2.a.string
        d['url']=one.h2.a['href']
        save(d)
        print('ok  ')
for url in url_list:
    jianmo(url)