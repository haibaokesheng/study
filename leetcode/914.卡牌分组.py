'''
@Author: your name
@Date: 2020-03-27 12:13:26
@LastEditTime: 2020-03-27 14:49:42
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\914.卡牌分组.py
'''
#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#
# https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
#
# algorithms
# Easy (32.96%)
# Likes:    112
# Dislikes: 0
# Total Accepted:    19.7K
# Total Submissions: 53.6K
# Testcase Example:  '[1,2,3,4,4,3,2,1]'
#
# 给定一副牌，每张牌上都写着一个整数。
# 
# 此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
# 
# 
# 每组都有 X 张牌。
# 组内所有的牌上都写着相同的整数。
# 
# 
# 仅当你可选的 X >= 2 时返回 true。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3,4,4,3,2,1]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
# 
# 
# 示例 2：
# 
# 输入：[1,1,1,2,2,2,3,3]
# 输出：false
# 解释：没有满足要求的分组。
# 
# 
# 示例 3：
# 
# 输入：[1]
# 输出：false
# 解释：没有满足要求的分组。
# 
# 
# 示例 4：
# 
# 输入：[1,1]
# 输出：true
# 解释：可行的分组是 [1,1]
# 
# 
# 示例 5：
# 
# 输入：[1,1,2,2,2,2]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[2,2]
# 
# 
# 
# 提示：
# 
# 
# 1 <= deck.length <= 10000
# 0 <= deck[i] < 10000
# 
# 
# 
# 
#

# @lc code=start
import collections 
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from fractions import gcd
        vals = collections.Counter(deck).values()
        print(vals)
        return reduce(gcd, vals) >= 2
        #可以先用短除法求其中两个数的最大公约数，
        #然后再用这个公约数和第三个数去求最大公约数

      

        

                 
        
# @lc code=end

