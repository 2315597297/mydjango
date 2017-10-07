import datetime
import threading

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from blog.models import Blog, Bankuai, Leixing
from home.seach import set_blog_context, get_seach_view
from media.bg_dir.get_pic import get_pic_url
#得到首页轮播推荐文章的算法
#推荐list
def gettuijian():
    # 可以内定的博客位
    neiding=[354,955,1030]
    lunbo_blog_list=[]
    # 转为blog对象，方便操作
    for bid in lunbo_blog_list:
        lunbo_blog_list.append(Blog.objects.get(id=bid))
    def getguankanblog(count):
        return Blog.objects.order_by('-yuedu')[:count]
    return getguankanblog(5)
# 分页页码
pagenum=16
# 得到分类和板块数据的方法
def getfenleicontext(context):
    context['bk_list'] = Bankuai.objects.all()
    context['lx_list'] = Leixing.objects.all()
    context['bg_img'] = get_pic_url()
    return context
# 得到博客文章列表的方法
def getContext(blogs,page,context):
    page = int(page)
    blogs_sum = len(blogs.all())
    if blogs_sum < ((page - 1) * pagenum):
        return False
    end = blogs_sum if blogs_sum < page * pagenum else page * pagenum
    context['zuixinbokewei'] = blogs.order_by('-pub_date')[(page - 1) * pagenum: end]
    web_page_sum = (blogs_sum // pagenum) + (1 if blogs_sum % pagenum > 0 else 0)
    context['pagesum'] = {'sum': list(range(1, web_page_sum + 1)), 'shang': [0 if page == 1 else 1, page - 1],
                          'dangqian': page, 'next': [0 if page == web_page_sum else 1, page + 1]}

    return getfenleicontext(context)


#-----------------------------------主页请求
def homepage(request,page=1):
    page=int(page)
    #全体博客
    blogs = Blog.objects
    #上传上下文
    context = {}
    #全体博客list
    context=getContext(blogs, page, context)
    if page==1:
        context['tuijian']=gettuijian()
    # context['pagenum'] = range(1,Paginator.num_pages)
    # print(Paginator.num_pages)
    # userlist=User.objects.order_by('money')[:5]
    # bloglist=Blog.objects.order_by('pub_date')[:6]
    # context['lunbo']=userlist[:3]
    # bloglen=Blog.objects.all().__len__()
    # if bloglen<10:
    #     context['zuixinbokewei'] = Blog.objects.order_by('-pub_date')
    # else:
    #     context['zuixinbokewei'] = Blog.objects.order_by('-pub_date')[:15]
    # context['paihang']=User.objects.order_by('-money')[:5]
    # context['xinyonghu']=User.objects.order_by('-pub_date')[:9]
    return render(request,'home/index.html',context)


#-----------------------------------id =板块ID   对应板块  请求
def mokuai(request,id,page=1):
    blog = Blog.objects.filter(bankuai=Bankuai.objects.filter(pk=id))
    for i in blog:
        print(i.title+str(i.id))
    context={}
    text = Bankuai.objects.get(pk=id)
    context=getContext(blog,page,context)
    context['text']=text
    context['urltype']='mokuai'
    context['id'] = id
    return render(request,'home/category.html',context)


#-----------------------------------id =类型ID   对应文章类型  请求
def leixing(request, id,page=1):
    blog = Blog.objects.filter(leixing=Leixing.objects.filter(id=id))
    context = {}
    text = Leixing.objects.get(pk=id)
    context = getContext(blog, page, context)
    context['text']=text
    context['urltype']='leixing'
    context['id']=id
    return render(request, 'home/category_l.html', context)

#----------------------------------- 显示所有模板 请求
def showmokuai(request):
    context = getfenleicontext({})
    return  render(request,'home/category_bankuai.html',context)
def filter(request,key):
    # context = getContext(blog, page, context)
    # context = {}
    # context['text'] = text
    # context['urltype'] = 'leixing'
    # context['id'] = id

    return


@require_http_methods(['POST'])
def seach(request):
    # ----------------------第一步  处理搜索键
    blog_list=[]
    b = Blog.objects.all()
    b_len = b.__len__()
    b_size = 0
    # KEY  要搜索的键
    key = request.POST.get('key')

    def list_fenduan(list_, count):
        fd_list = []
        c = 1
        while list_.__len__() > c * count:
            fd_list.append(list_[(c - 1) * count:c * count])
            c += 1
        fd_list.append(list_[(c - 1) * count:])
        return fd_list

    blog_fenduan_list = list_fenduan(b, 100)
    t_list=[]
    starttime = datetime.datetime.now()
    for fd_list in blog_fenduan_list:
        t = threading.Thread(target=set_blog_context, args=(key,fd_list,blog_list))
        t.start()
        t_list.append(t)
    for t in t_list:
        t.join()
    endtime = datetime.datetime.now()-starttime
    print(endtime)
    context={}
    context=getfenleicontext(context)
    blog_list= sorted(blog_list,reverse=True, key=lambda cd: cd['cd'])
    jiuguoshu=blog_list.__len__()
    if blog_list.__len__()>100:
        blog_list=blog_list[:100]
    context['blog_list']=get_seach_view(blog_list,key)
    # context['blog_list']=blog_list
    context['key']=key
    context['xiaolv']="检索了"+str(b_len)+"篇文章，"+str(jiuguoshu)+"条有效数据,服务器用时"+str(endtime)
    return render(request,'home/category_seach.html',context)
