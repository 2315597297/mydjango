from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$',views.show_blog,name='show_blog'),
    url(r'^add_blog/$', views.add_blog, name='add_blog'),
    url(r'^add_pinglun/$', views.add_pinglun, name='add_pinglun'),
    url(r'^add_blog/save_blog/$', views.save_blog, name='save_blog'),
    url(r'^drop_blog=(?P<id>[0-9]+)$',views.drop_blog,name='drop_blog'),
    url(r'^up_img$', views.up_img, name='up_img'),

]