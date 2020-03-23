# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:06:15 2020

@author: haibao
"""
class Solution:
    def getLeastNumbers(self, arr,k):
        if k==0:
            return []
        #最小的k个数 最大堆
        #最大堆 顶点最大
        def maxHeapfy(maxHeap,i,n):
            left=2*i+1
            right=2*i+2
            maxPoint=i
            if left<n and maxHeap[left]>maxHeap[maxPoint]:
                maxPoint=left
            if right<n and maxHeap[right]>maxHeap[maxPoint]:
                maxPoint=right
            if maxPoint!=i:
                maxHeap[i],maxHeap[maxPoint]=maxHeap[maxPoint],maxHeap[i]
                maxHeapfy(maxHeap,maxPoint,n)
        #初始化 取前k个树，组成最大堆
        maxHeap=arr[:k]
        #从第一个非叶子节点开始构建最大堆
        n=len(arr)
        for i in range(k//2-1,-1,-1):
            maxHeapfy(maxHeap,i,k)
        #继续调整后面节点
        for i in range(k,n):
            if arr[i]<maxHeap[0]:
                maxHeap[0]=arr[i]
                maxHeapfy(maxHeap,0,k)
        #现在全部构建好了，最后排序一次
        for i in range(k-1,0,-1):
            maxHeap[i],maxHeap[0]=maxHeap[0],maxHeap[i]
            maxHeapfy(maxHeap,0,i)
        return maxHeap
