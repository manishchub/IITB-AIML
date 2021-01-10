# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:47:16 2021

@author: manis
"""

#fibo which stores elements in a list

fib_nums = [0, 1]

n = 10

while len(fib_nums) < 10:
    fib_nums = fib_nums + [fib_nums[-1] + fib_nums[-2] ]

print (fib_nums)    

#fib_nums.append()