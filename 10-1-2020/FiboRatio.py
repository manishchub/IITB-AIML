# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 19:58:46 2021

@author: manish chellappan
"""

#Ratio of successive Fibo numbers

fib_nums = [0, 1]
fib_ratio = []
    
n=40
while len(fib_nums) < n:
  # fib_nums = fib_nums + [fib_nums[-1] + fib_nums[-2]]
  fib_nums.append(fib_nums[-1] + fib_nums[-2])
  if len(fib_nums) > 4:
   fib_ratio.append(fib_nums[-1] / fib_nums[-2])

print(fib_nums)
print()
print(fib_ratio)
