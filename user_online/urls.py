from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^login$',views.login,name='login'),
    url(r'^logout$',views.logout,name='logout'),
    url(r'^register$',views.register,name='register'),
    url(r'^logining$',views.logining,name='logining'),
    url(r'^registering$', views.registering, name='registering'),
    url(r'^existuser$',views.existuser,name='existuser'),
    url(r'^zhanghao/(?P<id>[0-9]+)$',views.zhanghao,name='zhanghao'),
    url(r'^upzhanghao$', views.upzhanghao, name='upzhanghao')
]