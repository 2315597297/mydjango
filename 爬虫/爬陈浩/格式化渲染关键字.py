# view = '''
# <article class="brick entry format-standard animate-this"  id='one_test' >
# <div class="entry-thumb">
#         <!-- 1 blogid -->
# <a href="%s" class="thumb-link">
#         <!-- 2 图片地址-->
# <img src="%s" alt="building">
# </a>
# </div>
# <div class="entry-text">
# <div class="entry-header">
# <div class="entry-meta">
# <span class="cat-links">
# <!--3 作者id  4 作者名-->
# <a href="%s">%s</a>
# <!--5 板块id  6 板块名-->
# <a href="%s">%s</a>
# </span>
# </div>
#                         <!--7 博客id  8 博客名-->
# <h1 class="entry-title"><a href="%s">%s</a></h1>
# </div>
# <div class="entry-excerpt">
# <!--  9 内容摘要-->
# %s
# </div>
# </div>
# </article> <!-- end article -->
#    '''%('/blog/682/','http://127.0.0.1:8000/media/blog_img/kukefengmian.png','/user_online/zhanghao/47','ch','/mokuai=2','酷壳网技术爬取','/blog/682/','正则表达式检查','摘要')
# print(view)
import re

a = '1asd正则表达asdasd式正则表达式表达式表达正则asdasd'
a=a.lower()
key  = 'ym[i].innerHTML=ym[i].innerHTML.replace(/([{{ key }}]{2,})/ig, "<span class=keyword>$1</span>");'
k = '正则表达式'
k=k.lower()
# print(k)
# print(a)
# s = re.match(r'.+?(['+str(k)+']{2,})(['+str(k)+']{2,})(['+str(k)+']{2,})',a)
# print(s)
# print(s.groups())
for s in list(k):
    a=a.replace(s,'<span class=keyword>'+s+'</span>')

print(a)
# a.re
# print(re.match('[aaa]{2,}','sadfasfaaa'))