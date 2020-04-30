# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:16:10 2020
@author: haibao
"""
# 1、定义两个指针，分别指向两个数列的第一个元素；定义新的空数列，作为结果。
# 2、依次取出指针值，比较大小，将较小值追加到新数列，同时将较小值的指针往后移动一位。
# 3、如果其中一个指针到头了，那么将另一个指针剩下的数列直接追加到结果数列即可。
# 4、直至两个指针都指到了最后一位。


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


def reversePairs(nums):

    count = 0  # 计数变量

    def merge_sort(alist):
        if len(alist) <= 1:
            return alist
        mid = len(alist)//2
        # 左闭右开区间
        left = merge_sort(alist[:mid])  # 注意切片的结果不包含结束索引，即不包含最后的一位
        right = merge_sort(alist[mid:])
        return merge(left, right)

    def merge(left, right):
        nonlocal count
        l, r = 0, 0
        result = []  # 辅助数组，记录排序好的
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:  # 右边的数字大
                result.append(right[r])
                r += 1
            # 归并的两个数组都是有序依次排列的，所以在执行归并的时候就会发现，
            # 若右边数组第r个元素（right[r]）大于左边数组第l个元素（left[l]），
            # 则右边数组的这个元素一定大于左边数组从第i个一直到最后一个元素。
            # 这样的话，第j元素对应的逆序数就是len（left）-l。
                count += len(left)-l
        result += left[l:]
        result += right[r:]
        return result
    merge_sort(nums)
    return count


if __name__ == '__main__':
    a = [2, 6, 10, 3, 5, 8, 41, 9]
    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print('排序后数组:', merge_sort(a))
    print('原数组的逆序对:', reversePairs(a))
