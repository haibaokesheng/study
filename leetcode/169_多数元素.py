'''
@Author: your name
@Date: 2020-03-13 21:33:32
@LastEditTime: 2020-04-05 20:25:14
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\169_多数元素.py
'''
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 21:33:03 2020

@author: haibao
2020.3.13leetcode 每日一题
同剑指offer的39题目
"""
#给定一个大小为 n 的数组，找到其中的多数元素。
#多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
class Solution:
    def majorityElement(self, nums) -> int:
        cnt = 0
        k = nums[0]
        for i,data in enumerate(nums):
            if data==k:
               cnt+=1
            else:
               cnt-=1
            if cnt == 0:
                k = nums[i+1]
        return k
a = Solution()
nums = [2,2,1,1,1,2,2] 
#nums = [3,2,3] 
print(a.majorityElement(nums))