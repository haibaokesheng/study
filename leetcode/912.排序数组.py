'''
@Author: your name
@Date: 2020-03-31 17:24:14
@LastEditTime: 2020-03-31 18:05:13
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\912.排序数组.py
'''
#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode-cn.com/problems/sort-an-array/description/
#
# algorithms
# Medium (53.03%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    40.9K
# Total Submissions: 69.5K
# Testcase Example:  '[5,2,3,1]'
#
# 给你一个整数数组 nums，请你将该数组升序排列。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
# 
# 
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def quick(left, right):
            if left >= right:
                return nums

            pivot = left
            i = left
            j = right
            while i < j:
                while  nums[j] > nums[pivot] and i < j:
                    j -= 1
                while  nums[i] <= nums[pivot] and i < j: 
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
                
            nums[pivot], nums[j] = nums[j], nums[pivot]
            
            quick(left, j - 1)
            quick(j + 1, right)
            return nums
            
        return quick(0, n - 1)


        
# @lc code=end

