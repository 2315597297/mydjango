import lxml
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from mydjango.settings import wangzhi, admin_leixing
from user_online.models import Profile

class Bankuai(models.Model):
    #板块的封面  可以为外链和内链 使用http://区分外链内链
    fengmian = models.ImageField(blank=False,upload_to='bankuai_img')
    #板块名称
    name = models.CharField(max_length=20)
    #关联到User对象  关联了即为专栏，专栏只有该User可以创建文章
    user = models.ForeignKey(User)
    #板块说明
    text = models.CharField(max_length=400)
    def get_name(self):
        if not self.user.username==admin_leixing:
            return '[专栏] '+self.name
        else:
            return self.name

    def get_fengmian_url(self):
        #区分外链内链   因为文件名不能使用/字符
        if 'https://' in self.fengmian or 'http://' in self.fengmian:
            return self.fengmian
        else:
            return wangzhi+self.fengmian.url

    def __str__(self):
        return self.name
class Leixing(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=400)
    def __str__(self):
        return self.name
class Blog(models.Model):
    title = models.CharField(max_length=100)
    fengmian = models.ImageField(blank=False,upload_to='blog_img')
    yuedu = models.IntegerField(default=0)
    content = models.TextField()
    # fangwenliang = models.IntegerField(default=0)
    zuozhe = models.ForeignKey(User)
    bankuai = models.ForeignKey(Bankuai)
    leixing = models.ForeignKey(Leixing)
    pub_date = models.DateTimeField()
    kuaizhao = models.TextField(max_length=70000)
    def __str__(self):
        return self.title
    def get_title(self):
        title=self.title
        if title.__len__()>26:
            return title[:26]+"..."
        return title
    def get_content(self):
        content=self.content
        bs = BeautifulSoup(content,'html.parser')
        bs=bs.text
        if bs:
            if bs.__len__()>60:
                return bs[:60]+'...'
        return bs
    def get_fengmian_url(self):
        # 区分外链内链   因为文件名不能使用/字符
        if 'https://' in self.fengmian.name or 'http://' in self.fengmian.name:
            return self.fengmian.name
        else:
            print(self.fengmian.url)
            print(self.fengmian.name)
            return wangzhi + self.fengmian.url


class Pinglun(models.Model):
    plzhe = models.ForeignKey(User)
    plblog = models.ForeignKey(Blog)
    pub_date = models.DateTimeField()
    pltext = models.CharField(max_length=1000)
    def __str__(self):
        return self.plblog.title