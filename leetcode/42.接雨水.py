'''
@Author: your name
@Date: 2020-04-04 22:02:13
@LastEditTime: 2020-04-05 00:05:03
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\42.接雨水.py
'''
#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (48.88%)
# Likes:    1124
# Dislikes: 0
# Total Accepted:    82.1K
# Total Submissions: 163.4K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 暴力法 第i个柱子能装的水是左右两侧最大值的较小值-i O(n^2) 
        # 超时 通过314个cases
        '''
        res = 0
        length = len(height)
        for i in range(length):
            left_max = 0
            right_max = 0
            for j in range(i):
                left_max = max(left_max,height[j])
            for j in range(i,length):
                right_max = max(right_max,height[j])
            if min(left_max,right_max)>height[i]:
                res += min(left_max,right_max)-height[i]
        return res   
        '''
        # 动态规划 使用备忘录记录第i个柱子左右两侧最大值 时间O(n),空间O(n)
        '''
        res = 0
        length = len(height)
        if length == 0:
            return 0
        left_max = [0] * length
        right_max = [0] * length
        left_max[0] = height[0]
        right_max[length-1] = height[length-1]
         
        for i in range(1,length):
            left_max[i] = max(left_max[i-1],height[i])
        for j in range(length-2,-1,-1):
            right_max[j] = max(right_max[j+1],height[j])
            
        for i in range(length):
            if min(left_max[i],right_max[i])>height[i]:
                res += min(left_max[i],right_max[i])-height[i]
        return res  
        ''' 
        # 双指针 
        # 找到最高点 
        # l = 0
        # r = len(height)-1
        # left_max = 0
        # right_max = 0
        # res = 0
        # while l<=r:
        #     if left_max<=right_max:
        #         if height[l]<left_max:
        #             res+= left_max-height[l]
        #             l+=1
        #             left_max = height[l]
                    
        #     else:
        #         if height[r]<right_max:
        #             res+= right_max-height[r]
        #             r-=1
        #             right_max = height[r]
                   
        # return res

# @lc code=end

