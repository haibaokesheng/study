# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:16:10 2020

@author: haibao
"""
#1、定义两个指针，分别指向两个数列的第一个元素；定义新的空数列，作为结果。
#2、依次取出指针值，比较大小，将较小值追加到新数列，同时将较小值的指针往后移动一位。
#3、如果其中一个指针到头了，那么将另一个指针剩下的数列直接追加到结果数列即可。
#4、直至两个指针都指到了最后一位。
def merge_sort(lists):
    '''
    递归进行归并排序。
    '''
    # 递归结束条件
    if len(lists) <= 1:
        return lists
    
    # 分治进行递归
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    
    # 将两个有序数组进行合并
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # 将较小值放入到result中
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 将未被扫描到的直接追加到result后面
    if i == len(left):
        result.extend(right[j:])
    else:
        result.extend(left[i:])
    
    return result
    
if __name__ == '__main__':
    a = [2, 6, 10, 3, 5, 8, 4]
    print(merge_sort(a))