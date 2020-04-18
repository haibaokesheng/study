'''
@Author: your name
@Date: 2020-04-11 20:22:22
@LastEditTime: 2020-04-11 21:09:12
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\15.三数之和.py
'''
#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (25.72%)
# Likes:    1990
# Dislikes: 0
# Total Accepted:    194.9K
# Total Submissions: 738.5K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums ):
        n = len(nums)
        res = []
        if not nums or n<3:
            return res
        nums.sort()
        for i in range(n):
            if (nums[i]>0):
                return res  ###
            if (i>0 and nums[i]==nums[i-1]):
                continue
            L = i+1
            R = n-1
            while L<R:
                if nums[i]+nums[L]+nums[R]==0:
                    res.append([nums[i],nums[L],nums[R]])
                    while (L<R and nums[L]==nums[L+1]):
                        L+=1
                    while (L<R and nums[R]==nums[R-1]):
                        R-=1
                    L+=1
                    R-=1
                elif (nums[i]+nums[L]+nums[R]>0):
                    R-=1 
                else: 
                    L+=1
        return res
# @lc code=end
a = Solution()
nums = [-1,0,1,2,-1,-4]
print(a.threeSum(nums))
