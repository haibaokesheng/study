# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:52:07 2020

@author: haibao
"""

class Solution:
    def merge(self, intervals) :
        if len(intervals) == 0:
            return []
        intervals.sort()
        ans = [intervals[0]]  ########
        for i in range(1, len(intervals)):
            if ans[-1][1] >= intervals[i][0]:#重叠的情况
                ans[-1] = [min(ans[-1][0], intervals[i][0]), max(ans[-1][1], intervals[i][1])]
            else:
                ans.append(intervals[i])
        return ans
a = Solution()
seq = [[1,3],[2,6],[8,10],[15,18]]


print(a.merge(seq))