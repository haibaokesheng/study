# -*- coding: utf-8 -*-

price = [9,11,8,5,7,12,16,14]

def stock_max_val(array):
    bef_min = array[0] #before_min_value
    res = [0]*len(array)
    i = 1
    while i<len(array):
        if array[i]<bef_min:
            bef_min = array[i]
        res[i] = array[i]-bef_min
        i+=1
    return bef_min#max(res)
print(stock_max_val(price))
    