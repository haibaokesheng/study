# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:11:55 2020

@author: haibao
"""

class Solution:
    def replaceSpace(self, s: str) -> str:
        i=0
        while i<len(s):
            if s[i]==" ":
                s = s[:i]+"%20"+s[i+1:]
                i+=3
                continue
            i+=1
        return s

        