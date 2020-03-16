# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:21:26 2020

@author: haibao
"""
class Solution:
    def isStraight(self, nums) -> bool:
        nums.sort()
        numOfZero, dis = nums.count(0), []
        for i in range(numOfZero + 1, 5):
            #print(i)
            if nums[i] == nums[i - 1]:
                return False
            dis.append(nums[i] - nums[i - 1] - 1)
        #print(dis)
        return sum(dis) <= numOfZero
        

a = Solution()
nums = [0,0,1,2,5]
print(a.isStraight(nums))