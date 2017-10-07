import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydjango.settings")# project_name 项目名称
django.setup()
import re

# ---------------------------------------单个博客比对方法
def get_mohu_seach_list(one_blog_list,blog,key_set,key_set_len,key_jiaocha_list):
    jingque_item = []
    changdu = 0
    titchangdu = 0
    for item in one_blog_list:
        # 将当前博客 切割后的 单个item的文字转为无序不重复set
        item_set = set(item)
        # 交集 key的set 与 当前item的set 得到二者之间共存的字符
        gongcunzhi = key_set & item_set
        # 相除得到当前共存值 与 key的符合度 超过70%即可详细比对
        if gongcunzhi.__len__() / key_set_len > 0.7:
            for huaci in key_jiaocha_list[changdu:]:
                bianhuabiaoji = jingque_item.__len__()
                for huaci_item in huaci:
                    if huaci_item in item:
                        if item in jingque_item:
                            jingque_item.remove(item)
                        jingque_item.append(item)
                        break
                # 说明 本次 划次list便利没有对精确结果产生变化，后续结果不用再看了
                if jingque_item.__len__() == bianhuabiaoji:
                    break
                if huaci[0].__len__() > changdu:
                    changdu = huaci[0].__len__()
    if jingque_item:
        print(jingque_item)
        content =''.join(jingque_item[-3:] if jingque_item.__len__() > 3 else jingque_item) + '...'
        if content.__len__() > 63:
            content = '' + content[-60:]
        for huaci in key_jiaocha_list[titchangdu:]:
            for huaci_item in huaci:
                if huaci_item in blog.title:
                    titchangdu=len(huaci_item)
                    break
        print(titchangdu)
        jieguoji = {'blog': blog, 'cd': changdu+titchangdu,'content': content}
        return jieguoji



def set_blog_context(key,b,blog_list):
    # 转为小写
    key = key.strip().lower()
    # 得到key的set值,最小化key的长度 后续代码会矫正key（如key=AAA这种）中重复字符的误差
    key_set = set(key)
    key_set_len = key_set.__len__()
    key_list = list(key)
    # 交叉的list 放入key中字符交叉list,用于精确匹配
    key_jiaocha_list = []
    # 将交叉list中各个字符交叉形成词组,词组分层级放入交叉list
    for i in range(1, key_list.__len__()):
        # 词组层级,由小及大,最小2个字符,固生BUG:key长为1无结果,外嵌if可解,然惰而不作
        ceng = []
        for index, a in enumerate(key_list[:-i]):
            value = a + ''.join(key_list[index + 1:index + 1 + i])
            ceng.append(value)
        key_jiaocha_list.append(ceng)

    for blog in b:
        # 分割方法  使用什么样的方式来分割item
        text = re.split(r'[,。，？\n]', blog.kuaizhao)
        list_ = get_mohu_seach_list(text, blog,key_set,key_set_len,key_jiaocha_list)
        if list_:
            blog_list.append(list_)


# 格式参照 {'blog': blog, 'cd': changdu+titchangdu,'content': content}
# 获得有关键字格式化的网页渲染
def get_seach_view(blog_list,key):
    views ='''
    
    '''
    for blog in blog_list:
        B = blog['blog']
        title = B.title
        zhaiyao = blog['content']
        title = title.lower()
        zhaiyao=zhaiyao.lower()
        t_list=[]
        z_list=[]
        for zy in list(zhaiyao):
            if zy in key:
                z_list.append('<span class=keyword>' + zy + '</span>')
            else:
                z_list.append(zy)
        for tit in list(title):
            if tit in key:
                t_list.append('<span class=keyword>' + tit + '</span>')
            else:
                t_list.append(tit)
        zhaiyao = ''.join(z_list)
        title = ''.join(t_list)
            # zhaiyao = zhaiyao.replace(k, '<span class=keyword>' + k + '</span>')
            # title = title.replace(k, '<span class=keyword>' + k + '</span>')

        blog_view = '''
            <article class="brick entry format-standard animate-this"  id='one_test' >
            <div class="entry-thumb">
                    <!-- 1 blogid -->
            <a href="%s" class="thumb-link" target="_blank">
                    <!-- 2 图片地址-->
            <img src="%s" alt="building">
            </a>
            </div>
            <div class="entry-text">
            <div class="entry-header">
            <div class="entry-meta">
            <span class="cat-links">
            <!--3 作者id  4 作者名-->
            <a href="%s" target="_blank">%s</a>
            <!--5 板块id  6 板块名-->
            <a href="%s" target="_blank">%s</a>
            </span>
            </div>
                                    <!--7 博客id  8 博客名-->
            <h1 class="entry-title" target="_blank"><a href="%s">%s</a></h1>
            </div>
            <div class="entry-excerpt">
            <!--  9 内容摘要-->
            %s
            </div>
            </div>
            </article> <!-- end article -->
            
            
               ''' % ('/blog/'+str(B.id)+'/',
                      B.get_fengmian_url(),
                      '/user_online/zhanghao/'+str(B.zuozhe.id),
                      str(B.zuozhe.first_name),
                      '/mokuai='+str(B.bankuai.id),
                      str(B.bankuai.name),
                      '/blog/'+str(B.id)+'/',
                      str(title),
                      str(zhaiyao))
        views+=blog_view
        print(B.title)
        print(B.get_fengmian_url)
    return views