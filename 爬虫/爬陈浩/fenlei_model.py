import os,django
from django.utils import timezone
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydjango.settings")# project_name 项目名称
django.setup()
from blog.views import getkuaizhao
from django.contrib.auth.models import User
from blog.models import Bankuai, Leixing, Blog


class fenlei(object):
    bk = Bankuai.objects.get(name='酷壳网技术爬取')
    lx = Leixing.objects.get(name='转载')
    pub_date = timezone.now()
    user = User.objects.get(username='ch')
    url =''
    fengmian = 'bankuai_img/qrcode_for_gh_dd9d8c843f20_860-300x300.jpg'

    def __init__(self,title,yuedu,content):
        self.title=title
        self.yuedu = yuedu
        self.content=content

    def save_blog(self):
        try:
            b = Blog(
            title=self.title,
            content=self.content,
            zuozhe=self.user,
            fengmian=self.fengmian,
            bankuai=self.bk,
            leixing=self.lx,
            yuedu=self.yuedu,
            pub_date=self.pub_date,
            kuaizhao=getkuaizhao(self.content)
            )
            b.save()
            # with open(self.title+".txt",'w') as f:
            #     f.write(self.content)
            print(self.title+'成功  ',end='')
            return False
        except Exception as e:
            print('\n')
            print(e)
            print(self.title+" "+self.url)
            return True

    def printblog(self):
        print(self.fengmian)
        print(self.yuedu)
        print(self.title)
        print(len(self.content))
        print('-----------------------------')