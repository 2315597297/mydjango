import os
import random

from mydjango.settings import wangzhi
img = os.listdir('C:\\Users\\xu\\PycharmProjects\\mydjango\\media\\bg_dir')
# 注意OS的工作路径不能更改，django使用os的工作路径来定位静态文件等操作
img.remove('get_pic.py')
img.remove('__pycache__')
# randint区间 [1,2]
def get_pic_url():
    # return wangzhi+'media/bg_dir/'+img[random.randint(0,img.__len__()-1)]
    return  wangzhi+'media/bg_dir/19.gif'
    pass

# for i in range(1,21):
#     print(get_pic_url())