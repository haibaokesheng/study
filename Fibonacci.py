# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:30:09 2020

@author: haibao
"""

def Fibonacci(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return n
  
    res = [0,1]
    for i in range(0,n-1):
        res.append(res[-1]+res[-2])
    return res

print(Fibonacci(15))
    