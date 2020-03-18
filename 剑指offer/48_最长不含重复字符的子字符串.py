# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:06:27 2020

@author: haibao
"""

class Solution:#时间复杂度O(n^2)
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0
        tail = 0
        if len(s) < 2: return len(s) # 边界条件
        res = 1
        
        while tail < len(s) - 1:
            tail += 1
            if s[tail] not in s[head: tail]:#python在列表中找元素是遍历，复杂度O(n)
                res = max(tail - head + 1, res) # 
            else:
                while s[tail] in s[head: tail]:
                    head += 1
        return res