import os,django

import re

import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydjango.settings")# project_name 项目名称
django.setup()

from blog.models import Blog
starttime = datetime.datetime.now()
b = Blog.objects.all()
# print('长度为：',len(b))
#
# def bijiao(key,k_list,i):
#     jiguo=[]
#     for l in k_list:
#         key = key.lower()
#         # ls=set(l)
#         # keys=set(key)
#         ls = set(l)
#         keys = set(key)
#         jj = ls & keys
#         jjj = jj.__len__() / keys.__len__()
#         if jjj > 0.9:
#             jiguo.append(l)
#     if jiguo:
#         return {'title':i,'j':jiguo}
#
# seach_j=[]
# for i in b:
#     text = re.split(r'[,。，？\n]', i.kuaizhao)
#     j = bijiao('base64',text,i.title)
#
#     if j:
#         seach_j.append(j)
#
#
# for i in seach_j:
#     print(i['title']+'返回',len(i['j']),'条结果：')
#     print(i['j'])
# endtime = datetime.datetime.now()
# print(endtime - starttime)

#----------------------第一步  处理搜索键
#KEY  要搜索的键
key = '6'
# 转为小写
keys= set(key.strip().lower())
keys_len = keys.__len__()
# 转为list  用作获取交叉list
key_list = list(key)
# 交叉 list 用于精确匹配
key_jiaocha_list=[]
# key 的长度,先打好提前量，以免在方法中多次获取
key_len = key.__len__()
for i in range(1, key_list.__len__()):
    ceng =[]
    for index, a in enumerate(key_list[:-i]):
        value = a + ''.join(key_list[index + 1:index + 1 + i])
        ceng.append(value)
    key_jiaocha_list.append(ceng)


#---------------------------------------单个博客比对方法
def get_mohu_seach_list(one_blog_list):
    jingque_item=[]
    changdu=0
    for item in one_blog_list:
        #将当前博客 切割后的 单个item的文字转为无序不重复set
        item_set = set(item)
        #交集 key的set 与 当前item的set 得到二者之间共存的字符
        gongcunzhi = keys & item_set
        # 相除得到当前共存值 与 key的符合度 超过70%即可详细比对
        if gongcunzhi.__len__() / keys_len>0.7:
            for huaci in key_jiaocha_list[changdu:]:
                bianhuabiaoji=jingque_item.__len__()
                for huaci_item in huaci:
                    if huaci_item in item:
                        if item in jingque_item:
                            jingque_item.remove(item)
                        jingque_item.append(item)
                        break
                # 说明 本次 划次list便利没有对精确结果产生变化，后续结果不用再看了
                if jingque_item.__len__()==bianhuabiaoji:
                    break
                if huaci[0].__len__()>changdu:
                    changdu=huaci[0].__len__()
    if jingque_item:
        print(jingque_item)
        content = '......'+''.join(jingque_item[-3:] if jingque_item.__len__() > 3 else jingque_item)+ '......'
        if content.__len__() > 63:
            content = '......'+content[-60:]
        jieguoji = {'id': id, 'cd': changdu, 'content': content}
        return jieguoji

for blog in b:
    print(blog.content.__sizeof__())
    text = re.split(r'[,。，？\n]', blog.kuaizhao)
    list_ = get_mohu_seach_list(text)
    if list_:
        print(list_)

endtime = datetime.datetime.now()
print(endtime - starttime)


