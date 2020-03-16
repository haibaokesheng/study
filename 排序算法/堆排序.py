# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 19:36:27 2019

@author: haibao
"""
def sift_down(arr, start, end):
    root = start
    while True:
        # 从root开始对最大堆调整
        child = 2 * root + 1
        if child > end:
            break
 
        # 找出两个child中交大的一个
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
 
        if arr[root] < arr[child]:
            # 最大堆小于较大的child, 交换顺序
            arr[root], arr[child] = arr[child], arr[root]
 
            # 正在调整的节点设置为root
            root = child
        else:
            # 无需调整的时候, 退出
            break
 
 
def heap_sort(arr):
    # 从最后一个有子节点的孩子还是调整最大堆
    first = len(arr) // 2 - 1
    for start in range(first, -1, -1):
        sift_down(arr, start, len(arr) - 1)
 
    # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
    for end in range(len(arr) -1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)
 
#def main():
#    # [7, 95, 73, 65, 60, 77, 28, 62, 43]
#    # [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
#    l = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
#    print (l)
#    heap_sort(l)
#    print (l)
 
 
if __name__ == "__main__":
 
    array = [16, 7, 3, 20, 17, 8]
    print(array)
    heap_sort(array)
    print(array)
