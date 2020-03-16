# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:39:04 2020

@author: haibao
2020.3.7 leetcode每日一题,队列的最大值 P288
"""
num = [2,3,4,2,6,2,5,1]
k = 3

def maxSlidingWindow(nums,k):
    quene_index,res = [],[]
    for i in range(len(nums)):
        if not quene_index:
            quene_index.append(i)
        else:
            if i == quene_index[0]+k:
                quene_index.pop(0)
            while quene_index and nums[quene_index[-1]]<num[i]:#若插入的数字大于队尾则弹出队头
                quene_index.pop()
            quene_index.append(i)

        res.append(num[quene_index[0]])
    return res[k-1:]
print(maxSlidingWindow(num,k))    
