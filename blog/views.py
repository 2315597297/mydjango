import os

from bs4 import BeautifulSoup
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ViewDoesNotExist, ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from blog.models import Blog, Bankuai, Leixing, Pinglun
from home.views import  getfenleicontext
from media.blog_img.save_img import save_img
from mydjango.settings import admin_leixing, wangzhi
from user_online.views import setmoney

#-----------------------------------显示博客 请求
def show_blog(request,id):
    try:
        context = {}
        print(id)
        b= Blog.objects.get(pk=id)
        # todo 必须使用 context['ss']=ss的形式
        context =getfenleicontext(context)
        context['blog']=b
        context['pinglun_list']=Pinglun.objects.filter(plblog=b)
        # print('asdss'+123)
        #阅读量加一
        b.yuedu+=1
        b.save()
        return render(request,'home/single-standard.html',context)
    except ObjectDoesNotExist :
        return error404(request,'你要找的文章不存在')
    except Exception as e:
        print(e)
        return error500(request,e)



#-----------------------------------写博客页面  请求
@login_required
def add_blog(request):
    bk_list=Bankuai.objects.filter(user__username=admin_leixing)|Bankuai.objects.filter(user=request.user)
    lx_list=Leixing.objects.all()
    return render(request,'add_blog.html',{'Bankuai':bk_list,'Leixing':lx_list})


class ImageUploadForm(forms.Form):
    """Image upload form."""
    picture = forms.ImageField()



#-----------------------------------保存博客 请求【提交网址】
# @csrf_exempt# 免掉token验证
@require_http_methods(['POST'])
@login_required
def save_blog(request):
    try:
        user = User.objects.get(pk=request.user.id)
        title = request.POST.get('title')
        bk = Bankuai.objects.get(pk=request.POST.get('bankuai'))
        lx = Leixing.objects.get(pk=request.POST.get('leixing'))
        content = request.POST.get('content')
        pub_date = timezone.now()
        b = Blog(
            title=title,
            content=content,
            zuozhe=user,
            bankuai=bk,
            leixing=lx,
            pub_date=pub_date,
            kuaizhao=getkuaizhao(content)
        )
        form = ImageUploadForm(request.POST, request.FILES)  # 有文件上传要传如两个字段
        if form.is_valid():
            b.fengmian = form.cleaned_data['picture']  # 直接在这里使用 字段名获取即可
            b.save()
            setmoney(user.id, len(content))
            print('ok')
        return HttpResponseRedirect("/blog/" + str(b.id))

    except Exception as e:
        return HttpResponse('保存失败！</br>非常抱歉，请将下方您编写的博客存根保存下来，或复制到编写区重新编写提交</br>注意！如果是重新编写可以直接复制到文本编辑区，如果是保存的话因为本站博客存根为HTML代码，不要直接保存在txt文本文档中，必要时可以右键查看源代码保存</br></br>'+content)

#-----------------------------------删除博客  【提交请求】
@login_required
def drop_blog(request,id):
    try :
        print(request.user.id)
        blog = Blog.objects.get(pk=id)
        if request.user.id == blog.zuozhe.id:
            blog.delete()
            return HttpResponseRedirect('/user_online/zhanghao/' + str(request.user.id))
        else:
            return HttpResponse('不是你的博客你删什么？？')
    except ObjectDoesNotExist as e:
        return error404(request,e,'该文章不存在这个地球上')
    except Exception as e:
        return  error500(request,e)



#-----------------------------------添加评论 【提交网址】
@require_http_methods(['POST'])
@login_required
def add_pinglun(request):
    # try :
    path = request.path
    print(path)
    plzhe = User.objects.get(pk=request.user.id)
    plblog = Blog.objects.get(pk=request.POST.get('plblog'))
    pltext = request.POST.get('pltext')
    pub_date = timezone.now()
    pl = Pinglun(plzhe=plzhe, plblog=plblog, pltext=pltext, pub_date=pub_date)
    setmoney(plzhe.id,len(pltext))
    pl.save()
    return HttpResponseRedirect(request.POST.get('blogurl'))

def getkuaizhao(content):
    text = BeautifulSoup(content,'lxml')
    content = text.text
    content = content.strip().lower()
    return content

def sm_pre(content):
    text = BeautifulSoup(content, 'lxml')
    if text.pre:
        for p in text.find_all('pre'):
            P_text = p.text
            # print(P_text)
            # print(type(P_text))
            # P_text.replaceAll("\r","</br>").replaceAll("\n","</br>")
            newtag= text.new_tag('pre')
            new_tag2= text.new_tag('code')
            new_tag2.string=P_text
            newtag.append(new_tag2)
            p.replace_with(newtag)
            if '\n' in P_text:
                print('我草拟老母')
    return str(text)

@csrf_exempt
@require_http_methods(['POST'])
def up_img(request):
    name = request.POST.get('key')
    # print(request.POST.FILES)
    img=request.FILES.get('file').file
    print(os.path)
    save_img(img,name)
    return HttpResponse(wangzhi+'media/blog_img/'+name)

def error404(request,e='',msg='抱歉,未找到请求的页面,请查看URL格式是否正确,或者提交返回给我'):
    context={}
    context['msg']=msg
    context['e']=e
    return render(request, 'error404.html',context)

def error500(request,e='',msg='抱歉,服务器出现了错误,请检查您所提交或请求的数据是否正确,或者提交反馈给我'):
    context={}
    context['msg']=msg
    context['e']=e
    return render(request, 'error500.html',context)
