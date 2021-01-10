# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 16:46:56 2021

@author: manis
"""

#fibonacci 0,1,1,2,3,5,8,...

a = 0
b = 1

for i in range (10):
    temp = b
    b = a + b
    a = temp
    print ('temp=' + str(temp) + ' a=' + str(a) + ' b=' + str(b))
    
