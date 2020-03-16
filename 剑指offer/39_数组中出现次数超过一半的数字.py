# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 21:33:03 2020

@author: haibao
2020.3.13leetcode 每日一题
同剑指offer的39题目
"""
#给定一个大小为 n 的数组，找到其中的多数元素。
#多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
class Solution: #摩尔投票法 O(n)
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

#class Soluton_2:
#    def MoreThanHalfArray(nums):
#        length = len(nums)
#        mid = >>1
#        start = 0
#        end = length-1
#        index = Partition(nums,)
        
class Soluton_3:
    def majorityElement(self,nums):
        if len(nums)==1:
            return nums[0]
        wirte = {}
        for i in nums:
            if i not in wirte:
                wirte[i]=1
            else:
                wirte[i]+=1
                if wirte[i]>(len(nums)/2):
                    return i
                

        
a = Solution()
a = Soluton_3()
nums = [2,2,1,1,1,2,2] 
#nums = [3,2,3] 
print(a.majorityElement(nums))