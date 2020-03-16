# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:36:39 2020

@author: haibao
2020.3.12

"""
#异或解法：异或运算满足交换律，a^b^a=a^a^b=b,
#因此ans相当于nums[0]^nums[1]^nums[2]^nums[3]^nums[4]..... 
#然后再根据交换律把相等的合并到一块儿进行异或（结果为0），
#然后再与只出现过一次的元素进行异或，这样最后的结果就是，只出现过一次的元素（0^任意值=任意值） 
nums = [3,4,3,4,1]
class Solution:
    def singleNumber(self, nums) -> int:
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number

a = Solution()
print(a.singleNumber(nums))