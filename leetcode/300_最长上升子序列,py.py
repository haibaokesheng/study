# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 09:54:43 2020

@author: haibao
leetcode 每日一题 3.14
300 最长上升子序列  动态规划
"""
#dp[i]的值代表以nums[i]结尾的最长子序列长度

class Solution:
    def lengthOfLIS(self, nums) -> int:
        size = len(nums)
        if size<=1:
            return size
        dp = [1]*size
        for i in range(1,size): # 遍历数组
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
nums = [10,9,2,5,3,7,101,18]
#nums = [2,2]
#nums = [9,8,7,6,5,4]
a = Solution()
print(a.lengthOfLIS(nums))
#print('最长上升子序列是 %d'%a.lengthOfLIS(nums))