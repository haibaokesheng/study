# -*- coding: utf-8 -*-
"""
排序算法学习
2019.4.28
"""
'''
1.冒泡排序 平均O(n^2),稳定算法
'''
def bubbleSort(nums):
    for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):  # ｊ为列表下标
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [1,4,7,8,5,2,3,6,9,0]

print (bubbleSort(nums))
'''
2.选择排序 O(n^2),不稳定算法 
'''
def select_sort(s):
    for i in range(len(s) - 1): #[0,i-1]是已经排序好的元素
        index = i
        for j in range(i + 1, len(s)): #第二层循环是从[i,length -1]中找到最小元素的下标，用来与i元素交换
            if s[index] > s[j]:
                index = j     #定义一个变量，用来记录本次循环下找到的最小元素的下标
        s[i], s[index] = s[index], s[i]
    return s
print(select_sort(nums))
'''
3.插入排序，越有序越快
'''
def insert_sort(alist):
    n = len(alist)
    for j in range(0, n): 
        for i in range(j, 0, -1):  #每次排序，有序队列中元素比较替换的次数 即"比较循环"
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            else:
                break
    return alist
print(insert_sort(nums))
'''
4.快速排序nlogn
'''
def QuickSort(myList,start,end):
    #判断low是否小于high,如果为false,直接返回
    if start < end:
        i,j = start,end
        #设置基准数
        base = myList[i]

        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1
            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]
            #同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base
        #递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList
print(QuickSort(nums,0,len(nums)-1))

'''
5.希尔排序,缩小增量排序
'''
def shell_sort(l):
    n = len(l)
    # 初始间隔
    gap = n//2
    
    while gap > 0:
        for i in range(gap, n):
            for j in range(i, gap-1, -gap):
                if l[j] < l[j-gap]:
                    l[j], l[j-gap] = l[j-gap], l[j]
                else:
                    break
        gap //= 2
    return l

l = shell_sort(nums)

'''
堆排序 2019.9.7
'''
def sift(data, low, high):
    i = low      # 父节点
    j = 2 * i + 1   # 左子节点
    tmp = data[i]   # 父节点值
    while j <= high:    # 子节点在节点中
        if j < high and data[j] > data[j + 1]:  # 有右子节点且右节点比父节点值大
            j += 1
        if tmp > data[j]:
            data[i] = data[j]   # 将父节点替换成新的子节点的值
            i = j   # 变成新的父节点
            j = 2 * i + 1   # 新的子节点
        else:
            break
    data[i] = tmp   # 将替换的父节点值赋给最终的父节点


def heap_sort(data):
    n = len(data)
    # 创建堆
    for i in range(n//2-1, -1, -1):
        sift(data, i, n-1)

    # 挨个出数
    for i in range(n-1, -1, -1):    # 从大到小
        data[0], data[i] = data[i], data[0]     # 将最后一个值与父节点交互位置
        sift(data, 0, i-1)



print(heap_sort(nums))



def bubble_sort(n):
    for i in range(len(n)-1):
        for j in range(len(n)-i-1):
            if n [j]>n[j+1]:
                n[j],n[j+1] =n[j+1],n[j]
                
    return n
print(bubble_sort([5,4,9,1,15,1,0]))    




    