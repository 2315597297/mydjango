import os


def save_img(img,name):
    print(os.getcwd())
    with open(os.getcwd()+'\\media\\blog_img\\'+name, 'wb') as f:
        f.write(img.getvalue())