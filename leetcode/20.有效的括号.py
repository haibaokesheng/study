'''
@Author: your name
@Date: 2020-04-01 18:59:35
@LastEditTime: 2020-04-01 19:07:49
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\20.有效的括号.py
'''
#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.97%)
# Likes:    1476
# Dislikes: 0
# Total Accepted:    241.3K
# Total Submissions: 584.5K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic ={'{':'}','[':']','(':')',"?":"?"}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()]!=c:
                return False
        return len(stack)==1
            
        
# @lc code=end

