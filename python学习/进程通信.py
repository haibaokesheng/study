'''
@Author: your name
@Date: 2020-03-26 13:56:57
@LastEditTime: 2020-03-26 14:11:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\python学习\进程通信.py
'''
from multiprocessing import Process,Queue
from time import sleep
def download(q):
    images=['girl.jpg','boy.jpg','man.jpg']
    for image in images:
        print('正在下载:',image)
        sleep(0.5)
        q.put(image)
        
def getfile(q):
    while True:
        try:
            file = q.get(timeout=5)
            print('{} 保存成功！'.format(file))
        except:
            print('全部保存完毕')
            break
    
if __name__ == "__main__":
    q = Queue(5)
    p1 = Process(target=download,args=(q,))
    p2 = Process(target=getfile,args=(q,))

    p1.start()
    p1.join()
    p2.start()
    p2.join()

    print('0000000')