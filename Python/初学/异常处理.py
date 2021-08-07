# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 21:45:03 2021

@author: tizen
"""

empIDList = ['1','2','3']
try:
    empIDList.remove(4)
except:
    print('could not remove')
print('after remove')
print('='*20)

def calAvg(total,number):
    try:
        return total/number
    except(ZeroDivisionError,TypeError,Exception) as e:
        print('err: '+ str(e))
print(calAvg(100,2)) #right
print(calAvg(100,0)) # zero division
print(calAvg(100, '2')) #type error
print('continue')
print('='*20)

