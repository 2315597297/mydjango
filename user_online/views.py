import random

from django import contrib
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login
# Create your views here.
from blog.models import Blog, Pinglun, Bankuai
from home.views import homepage
from mydjango.settings import wangzhi


#-----------------------------------登录 请求
def login(request):
    return render(request,'login.html')

#-----------------------------------登出 【提交】
def logout(request):
    contrib.auth.logout(request)
    return homepage(request)

#-----------------------------------注册 请求
def register(request):
    return render(request,'register.html')


#-----------------------------------登录 【提交】
@require_http_methods(['POST'])
def logining(request):
    user = authenticate(username=request.POST.get('user'), password=request.POST.get('passwd'))
    if user is not None:
        # the password verified for the user
        if user.is_active:
            contrib.auth.login(request, user)
            print("User is valid, active and authenticated")
            return HttpResponseRedirect(wangzhi)
        else:
            print("The password is valid, but the account has been disabled!")
            return HttpResponse('<html><body>用户名或者密码错误！</body></html>')
    else:
        # the authentication system was unable to verify the username and password
        print("The username and password were incorrect.")
        return HttpResponse('<html><body>用户名或者密码错误！</html></body>')


# -----------------------------------注册  【提交】
@require_http_methods(['POST'])
def registering(request):
    try:
        user=request.POST.get('user')
        passwd= request.POST.get('passwd')
        if passwd.__len__()<8:
            return HttpResponse('密码请大于8位 不要枢无意义的中文，数据库能存但以后会出问题')
        # (username = user, password = passwd, first_name = user, last_name = '这个人很懒没有个人签名')
        u = User.objects.create_user(user,'999@iox.mns',passwd)
        u.save()
        u.first_name=user
        u.last_name = '这个人很懒没有个人签名'
        u.profile.touxiang='User_tx/admin_tx/tx_'+str(random.randint(0, 9))+'.gif'
        u.save()
    except Exception:
        return HttpResponse('请您好好填写数据  我没有时间去网页做那些验证，但是服务器是有的')
    return HttpResponseRedirect(wangzhi)

#----------------------------------检测用户名合法性 【提交】
@csrf_exempt# 免掉token验证
@require_http_methods(['POST'])
def existuser(request):
    user = request.POST.get('user')
    if user =='':
        return HttpResponse('你输入的用户名不和谐')
    weijin_list=[
        '江泽民','徐成','飞','None','NULL','null',' '
    ]
    for weijin in weijin_list:
        if weijin in user:
            return HttpResponse('你输入的用户名不和谐')
    if User.objects.filter(username=user):
        return HttpResponse('用户名已存在')
    return HttpResponse('用户名可以使用')


#-----------------------------------查看账号信息 请求
@login_required
def zhanghao(request,id):
    user=User.objects.get(pk=id)
    blogs = Blog.objects.filter(zuozhe=user)
    context={}
    context['seeuser']=user
    context['wzshu'] = len(blogs.all())
    context['plshu'] = len((Pinglun.objects.filter(plzhe=user)).all())
    context['blogs']=blogs
    context['zl'] = Bankuai.objects.filter(user=user).all()
    return render(request, 'zhanghao.html', context)


#----------------------------------- 修改账号 【提交】
class ImageUploadForm(forms.Form):
    """Image upload form."""
    picture = forms.ImageField()
@require_http_methods(['POST'])
@login_required
def upzhanghao(request):
    user = User.objects.get(pk=request.user.id)
    form = ImageUploadForm(request.POST, request.FILES)  # 有文件上传要传如两个字段
    if form.is_valid():
        user.profile.touxiang = form.cleaned_data['picture']  # 直接在这里使用 字段名获取即可
    user.first_name=request.POST.get('nickname')
    user.last_name=request.POST.get('jieshao')
    user.save()
    return HttpResponse('修改成功')

def setmoney(id,lengh):
    user= User.objects.get(pk=id)
    user.profile.money+=lengh*100
    user.save()
    pass
