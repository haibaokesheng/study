# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:41:10 2020

@author: haibao
双指针
"""
list_1 = [1,2,4,7,11,15]
s = 15
def FindNumbersWithSum(array,s):
    i = 0
    j = len(array)-1
    while j>i:
        sum = array[i]+array[j]
        if sum == s:
            return array[i],array[j]
        elif  s<sum:
            j-=1
        else:
            i+=1
#print(FindNumbersWithSum(list_1,s))


"""
2020.3.6 leetcode每日一题,和为s的连续正数数列 P282
"""
#输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
target = 19
def FindContinuousSequence(target):
    i = 1
    j = 2
    res = []
    sum = i+j
    while i<=(target//2):##### 
        if sum < target:
            j+=1
            sum += j
        elif sum > target:
            sum -=i
            i+=1    
        else:
            res.append(list(range(i,j+1)))
            j+=1
            sum += j
    return res
print(FindContinuousSequence(target))