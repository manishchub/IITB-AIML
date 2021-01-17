# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 14:44:07 2021

@author: manis
"""

#sum of cubes
sum_of_cubes = []
sum_of_cubes= ["i=" + str(i) + " j=" + str(j) + " " + \
    str(i**3 + j**3) for i in range(1 , 20) \
              for j in range(1 , 20 )  if i <= j and (i**3 + j**3) == 1729 ]
#sum_of_cubes= [ i**3 + j**3 for i in range(1 , 20) \
#                for j in range(1 , 20 )  if i <= j ]
sum_of_cubes.sort()
print(sum_of_cubes)
