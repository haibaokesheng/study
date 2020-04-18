'''
@Author: your name
@Date: 2020-03-28 13:18:06
@LastEditTime: 2020-03-28 18:36:06
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\leetcode\820.单词的压缩编码.py
'''
#
# @lc app=leetcode.cn id=820 lang=python3
#
# [820] 单词的压缩编码
#
# https://leetcode-cn.com/problems/short-encoding-of-words/description/
#
# algorithms
# Medium (40.27%)
# Likes:    91
# Dislikes: 0
# Total Accepted:    17.9K
# Total Submissions: 40.3K
# Testcase Example:  '["time", "me", "bell"]'
#
# 给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
# 
# 例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0,
# 2, 5]。
# 
# 对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
# 
# 那么成功对给定单词列表进行编码的最小字符串长度是多少呢？
# 
# 
# 
# 示例：
# 
# 输入: words = ["time", "me", "bell"]
# 输出: 10
# 说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= words.length <= 2000
# 1 <= words[i].length <= 7
# 每个单词都是小写字母 。
# 
# 
#

# @lc code=start
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(words, key = lambda i: len(i), reverse=True)
        print(words)
        s = ""
        for i in words:
            if i+"#" in s:
                continue
            s += i+"#"
        print(s)
        return len(s)



        
        
# @lc code=end

