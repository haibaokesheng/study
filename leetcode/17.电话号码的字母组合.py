'''
@Author: your name
@Date: 2020-04-09 13:27:22
@LastEditTime: 2020-04-09 13:56:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \leetcode\17.电话号码的字母组合.py
'''
#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (52.74%)
# Likes:    651
# Dislikes: 0
# Total Accepted:    98.6K
# Total Submissions: 185.6K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 示例:
# 
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
# 
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = [' ','','abc','def','ghi',
        'jkl','mno','pqrs','tuv','wxyz']
        res = []
        if(len(digits))==0:
            return []
        # digits 数字
        # index 数字的索引
        # path 已经编码的字符
        #回溯法的代码套路是使用两个变量：
        # res 和 path，res 表示最终的结果，path 保存已经走过的路径。
        # 如果搜到一个状态满足题目要求，就把 path 放到 res 中。
        def FindCombinations(digits,index,path):
            if index == len(digits):       
                return res.append(path)
            c = digits[index]
            letters = letterMap[int(c)]
            for i in letters:
                FindCombinations(digits,index+1,path+i)

        FindCombinations(digits,0,"")
        return res
# @lc code=end

