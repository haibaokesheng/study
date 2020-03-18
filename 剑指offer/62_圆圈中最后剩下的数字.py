# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:14:07 2020

@author: haibao
"""
def LastRemaining(m,n):
    last = 0
    for i in range(2,n+1):
        last = (last+m)%i
    return last
