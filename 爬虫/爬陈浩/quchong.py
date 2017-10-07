import os,django
from django.utils import timezone
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydjango.settings")# project_name 项目名称
django.setup()
import requests
from bs4 import BeautifulSoup
import pymysql

from blog.models import Blog

#可以查看酷壳网与本地数据库博客中的数据交叉结果
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
def quchong():
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
gong = quchong()
b_list = Blog.objects.all()
print(type(gong))
for g in gong:
    if Blog.objects.filter(title=g[1]):
        sql = 'delete from pachong_test.kuke_copy where id=%s'
        cursor.execute(sql,(g[0]))
        # 提交
        dbObject.commit()
        print('删除了：'+str(g[1]))