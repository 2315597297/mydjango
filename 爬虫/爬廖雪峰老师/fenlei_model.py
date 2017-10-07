import os,django
from django.utils import timezone
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydjango.settings")# project_name 项目名称
django.setup()
from blog.views import getkuaizhao
from django.contrib.auth.models import User
from blog.models import Bankuai, Leixing, Blog


class fenlei(object):
    bk = Bankuai.objects.get(name='廖雪峰python基础教程')
    lx = Leixing.objects.get(name='转载')
    fengmian = 'blog_img/0.png'
    pub_date = timezone.now()
    user = User.objects.get(username='lxf')
    def __init__(self,title,content):
        self.title=title
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
            pub_date=self.pub_date,
            kuaizhao=getkuaizhao(self.title+"\n"+self.content)
            )
            b.save()
            # with open(self.title+".txt",'w') as f:
            #     f.write(self.content)
            print(self.title+'成功')
            return False
        except Exception as e:
            print(e)
            return True
