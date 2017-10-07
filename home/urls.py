from django.conf.urls import url

from home import views

urlpatterns=[
   url(r'^$',views.homepage,name='home'),
   url(r'^(?P<page>[0-9]+)$', views.homepage),
   url(r'^mokuai=(?P<id>[0-9]+)$',views.mokuai,name='mokuai'),
   url(r'^mokuai=(?P<id>[0-9]+)/(?P<page>[0-9]+)$',views.mokuai,name='mokuai='),
   url(r'^leixing=(?P<id>[0-9]+)$', views.leixing, name='leixing'),
   url(r'^leixing=(?P<id>[0-9]+)page=(?P<page>[0-9]+)$', views.leixing, name='leixing='),
   url(r'^showmokuai$', views.showmokuai, name='showmokuai'),
   url(r'^seach$',views.seach,name='seach'),
   # url(r'^mokuai=(?P<id>[0-9]+)/(?P<page>[0-9]+)$', views.mokuai, name='mokuai'),
]