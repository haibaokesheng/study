'''
@Author: your name
@Date: 2020-04-13 18:03:53
@LastEditTime: 2020-04-13 18:41:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\46.全排列.py
'''
#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (74.17%)
# Likes:    609
# Dislikes: 0
# Total Accepted:    101.9K
# Total Submissions: 136.5K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        LinkedList result = new LinkedList();
        public void backtrack(路径，选择列表)
            if(满足结束条件)
                result.add(结果)
            for(选择：选择列表)
                做出选择;
                backtrack(路径，选择列表);
                撤销选择;   
        '''
        def backtrack(res, path, nums):
            if len(nums) == 0:
                res.append(path[:])
                print(res)
                return
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(res, path, nums[:i] + nums[i+1:])
                path.pop()

        res = []
        path = []
        backtrack(res, path, nums)
        return res
# @lc code=end

