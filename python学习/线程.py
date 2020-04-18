'''
@Author: your name
@Date: 2020-03-26 14:27:48
@LastEditTime: 2020-03-26 16:29:47
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\python学习\线程.py
'''
'''
线程：新建 就绪 运行 阻塞 结束
进程里可以存多个线程，多个线程共享进程资源
GIL  全局解释器锁
线程 ‘伪线程’
进程：
'''
import threading
from time import sleep
def download(n):
    images=['girl.jpg','boy.jpg','man.jpg']
    for image in images:
        print('正在下载:',image)
        sleep(n)
        print('下载{}成功！'.format(image))
def listenMusic():
    musics=['大碗快','好的','面包大王','伟大']
    for music in musics:
        sleep(0.5)
        print('正在听{}歌'.format(music))
if __name__ == "__main__":
    #线程对象
    t = threading.Thread(target=download,name='aa',args=(1,))
    t.start()
    t1 = threading.Thread(target=listenMusic,name='aa')
    t1.start()
    # n = 1
    # while True:
    #     print(n)
    #     sleep(1.5)
    #     n+=1