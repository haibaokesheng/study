# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:01:17 2020

@author: haibao
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_S = []
        stack_T = []
        for letter in S:
            if letter !="#":
                stack_S.append(letter)
            elif stack_S:
                stack_S.pop()

        for letter in T:
            if letter !="#":
                stack_T.append(letter)
            elif stack_T:
                stack_T.pop()
        return stack_S==stack_T
a = Solution()
S = "ab##"
T = "c#d#"
print(a.backspaceCompare(S,T))