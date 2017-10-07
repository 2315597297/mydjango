"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import django
from django.conf import settings
from django.conf.urls import include, url, handler404, handler500
from django.contrib import admin
from django.conf.urls.static import static

from blog.views import error404, error500

handler404 = error404
handler500 = error500
handler403 = error500

urlpatterns = [
    url(r'^',include('home.urls',namespace='home')),
    url(r'^user_online/',include('user_online.urls',namespace='online')),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/',include('blog.urls',namespace='blog')),
    url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
