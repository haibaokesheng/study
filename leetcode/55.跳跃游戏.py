#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode-cn.com/problems/jump-game/description/
#
# algorithms
# Medium (38.21%)
# Likes:    571
# Dislikes: 0
# Total Accepted:    86.6K
# Total Submissions: 220.9K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 判断你是否能够到达最后一个位置。
# 
# 示例 1:
# 
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
# 
# 
# 示例 2:
# 
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
# 
# 
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        # energy = 0
        # for i in range(n):
        #     energy = max(energy-1,nums[i])
        #     if energy<=0 and i<n-1:
        #         return False
        # return True
        
        right_max = nums[0]
        for i in range(n):
            if i<=right_max:###可以到达i
                right_max = max(right_max,i+nums[i])
                if right_max>=n-1:
                    return True
        return False
# @lc code=end

