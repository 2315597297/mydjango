import threading

# 为线程创建一个方法
from time import sleep

count = 20
lists =[ x for x in range(1,101)]

def thread(list_):
    for  i in list_:
        sleep(1)
        print(threading.current_thread().name+':'+str(i))

def list_fenduan(list_,count):
    fd_list =[]
    c = 1
    while list_.__len__()>c*count:
        fd_list.append(list_[(c-1)*count:c*count])
        c+=1
    fd_list.append(list_[(c - 1) * count:])
    return fd_list

fenrenwu_list = list_fenduan(lists,count)
for t_list in fenrenwu_list:
    t= threading.Thread(target=thread,args=(t_list,),name=t_list[0])
    t.start()
    # t.join()