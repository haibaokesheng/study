'''
@Author: your name
@Date: 2020-03-26 11:57:14
@LastEditTime: 2020-03-26 12:55:56
@LastEditors: Please set LastEditors
@Description: 进程池 学习
@FilePath: \刷题人生\python学习\进程池.py
'''
from multiprocessing import Pool
# 非阻塞式进程:全部添加到队列中，立刻返回，并没有等待其他进程执行完毕，但是回调函数是等待任务完成之后才调用
import time
import os
from random import random
def task(task_name):
    print('开始做任务啦!',task_name)
    start = time.time()
    time.sleep(random()*2)
    end = time.time()
    #print('完成任务:{} 用时:{} 进程id:{}'.format(task_name,(end-start),os.getpid()))
    return '完成任务:{} 用时:{} 进程id:{}'.format(task_name,(end-start),os.getpid())
container = []
def callback_func(n):
    container.append(n)
if __name__=='__main__':
    pool = Pool(5)
    tasks = ['听音乐','吃饭','洗衣服','打游戏','散步','看孩子','做饭']
    for  task1 in tasks:
        pool.apply_async(task,args=(task1,),callback=callback_func)
    pool.close() # 添加任务结束
    pool.join()  #
    for c in container:
        print(c)
    print('over!!!!!')