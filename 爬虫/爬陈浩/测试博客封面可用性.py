import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydjango.settings")# project_name 项目名称
django.setup()
import requests
from blog.models import Blog
import threading

def xiugai(blog,xiugaishu):
    xiugaishu+=1
    print('----------------------修改了'+str(xiugaishu)+'个------------------------------修改了' + blog.title + "的封面")
    blog.fengmian = 'blog_img/kukefengmian.png'
    blog.save()

xiugaishu=0
blog_list = Blog.objects.all()
cur = 0
blog_count = len(blog_list)
def getimg(b_list):
    for blog in b_list:
        f = blog.fengmian.name
        if 'https://' in f or 'http://' in f:
            if f == 'https://coolshell.cn/imgs/100offer_600_200.png':
                print('修改了100offer' + blog.title + "的封面")
                blog.fengmian = 'blog_img/kukefengmian.png'
                blog.save()
            else:
                try:
                    resp = requests.get(f)
                    if not resp.status_code==200:
                       xiugai(blog,xiugaishu)
                    print(blog.title+'  :过')
                except Exception as e:
                    xiugai(blog,xiugaishu)
        else:
            print(blog.title+'  :过')


def list_fenduan(list_,count):
    fd_list =[]
    c = 1
    while list_.__len__()>c*count:
        fd_list.append(list_[(c-1)*count:c*count])
        c+=1
    fd_list.append(list_[(c - 1) * count:])
    return fd_list

blog_fenduan_list = list_fenduan(blog_list,100)
for fd_list in  blog_fenduan_list:
    t = threading.Thread(target=getimg,args=(fd_list,))
    t.start()



