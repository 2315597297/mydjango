from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from mydjango.settings import wangzhi


class Profile(models.Model):
    # user 的email不要
         # frist_name 为昵称
         # last_name 为个人简介
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    touxiang = models.ImageField(upload_to='User_tx')
    money = models.BigIntegerField(default=0)

    def __str__(self):
        return self.user.first_name
    def get_touxiang_url(self):
        return wangzhi+self.touxiang.url
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Profile.objects.create(user=instance)
        Profile.objects.create(id=instance.id,user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# class myUser(models.Model):
#     # user 的email不要
#     # frist_name 为昵称
#     # last_name 为个人简介
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     touxiang = models.ImageField(upload_to='User_tx',blank=True)
#     money = models.BigIntegerField(default=0)
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         myUser.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
    # nicheng = models.CharField(max_length=10,unique=True)
    # passwd = models.CharField(max_length=20)
    # touxiang = models.ImageField(upload_to='User_tx')
    # gerenjianjie = models.CharField(max_length=300,default='我是个大懒人，所以没有个人介绍')
    # money = models.BigIntegerField(default=0)
    # pub_date = models.DateTimeField()
    # def __str__(self):
    #     return self.nicheng