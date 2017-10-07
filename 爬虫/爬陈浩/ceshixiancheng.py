import random
import threading
from time import sleep


def p():
   for i in range(1,9):
       sleep(random.randint(1, 3))
       print(threading.current_thread().name + "正在执行")

name=['q','w','e','f','i','j']
tt = []
for n in  name:
    t = threading.Thread(target=p, name=n)
    t.start()
    tt.append(t)
for t in tt:
    t.join()

# t = threading.Thread(target=p, name=name[0])
# t.start()
# t2 = threading.Thread(target=p, name=name[1])
# t2.start()
# t3 = threading.Thread(target=p, name=name[2])
# t3.start()
# t4 = threading.Thread(target=p, name=name[3])
# t4.start()
# t5 = threading.Thread(target=p, name=name[4])
# t5.start()
# t6 = threading.Thread(target=p, name=name[5])
# t6.start()
#
# t.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# t6.join()



print('asdfsdafqqqqqq')