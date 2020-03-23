# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:17:03 2020

@author: haibao
2020.3.19leetcode每日一题 最长回文串
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<2:
            return len(s)
        res = 0
        letter = {}
        for i in s:
            if i not in letter:
                letter[i]=1
            else:
                letter[i]+=1
        flag = False     # flag变量用于统计出现奇数次的字母
        for i in letter:
            print(i,letter[i])
            #if letter[i]%2==0: # 出现偶数次，那么就把该字母的个数都加上    %是取余
            if letter[i]&1==0:  # & 位与 ,奇数的最后一位 is 1, 偶数是 0
                res += letter[i]
            else:  #出现奇数次
                if not flag: #flag为False，把该字母的个数都加上
                    res+= letter[i]
                    flag = True
                else:       #flag为True，那么就应加上该字母的个数减一
                    res +=letter[i]-1 
        return res
a = Solution()
s = "abccccdd"
print(a.longestPalindrome(s))

