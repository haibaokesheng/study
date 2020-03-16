# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:40:59 2020

@author: haibao
"""

def binarySearch(nums,target):
    left = 0
    right = len(nums) - 1; # 注意

    while left <= right: 
        mid = left + (right - left) // 2;
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            left = mid + 1; # 注意
        elif nums[mid] > target:
            right = mid - 1# 注意
    return -1;
nums = [1,2,2,2,3]
nums = [1,2,3,4,5,6,7,8,9,10]
target = 2
print(binarySearch(nums,target))