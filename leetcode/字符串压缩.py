# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 08:50:54 2020

@author: haibao
"""

class Solution:
    def compressString(self, S: str) -> str:
        n=len(S)
        if n<=2:
            return S

        ans=S[0]
        count=1
        for i in range(1,n):
            if S[i]==S[i-1]:
                count+=1
            else:
                ans += str(count)+S[i]
                count=1
        ans+=str(count)
        # print(ans)
        len_ans=len(ans)
        return  ans if len_ans<n else S
    
a = Solution()
S = "aabcccccaa"
print(a.compressString(S))