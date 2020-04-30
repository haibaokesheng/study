#
# @lc app=leetcode.cn id=1248 lang=python3
#
# [1248] 统计「优美子数组」
#
# https://leetcode-cn.com/problems/count-number-of-nice-subarrays/description/
#
# algorithms
# Medium (47.08%)
# Likes:    79
# Dislikes: 0
# Total Accepted:    15.1K
# Total Submissions: 28.5K
# Testcase Example:  '[1,1,2,1,1]\n3'
#
# 给你一个整数数组 nums 和一个整数 k。
# 
# 如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
# 
# 请返回这个数组中「优美子数组」的数目。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,1,2,1,1], k = 3
# 输出：2
# 解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
# 
# 
# 示例 2：
# 
# 输入：nums = [2,4,6], k = 1
# 输出：0
# 解释：数列中不包含任何奇数，所以不存在优美子数组。
# 
# 
# 示例 3：
# 
# 输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# 输出：16
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length
# 
# 
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        '''
        双指针指向连续k个奇数的两端，每次计算当前状态下的子数组个数，
        计算方法为(左指针到上一个奇数之间的偶数个数+1) * (右指针到下一个奇数之间的偶数个数+1)，
        然后同时向后移动左右指针再进行下一轮的计算直到右指针到达边界。
        每一轮计算的累加和就是最终要求的所有子数组的个数
        '''
        nums = [x if x%2==1 else 0 for x in nums ]
        print(nums)
        
# @lc code=end

