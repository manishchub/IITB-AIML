# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 16:27:09 2021

@author: manis
"""
#Guess number game
#Unknown
#will tell you greater or less

import random

magicnumber = random.randint(1, 100)
guess = -1
i = 1
max = input ('enter guess count: ')


while guess != magicnumber and i <= int(max):

             
        num = input('enter your guess: ')
        guess = int(num)
        print ('max is ' + str(max) + ' and i is ' + str(i) )
        
        if guess < magicnumber:
            print('You entered ' + str(guess) + ' which is low')
        elif guess > magicnumber:
            print('You entered ' + str(guess) + ' which is high')
        else:
            print('match')
            break
        
        # if i == int(max):
        #     print('sorry exhausted chances.. :( ')
        #     break
        
        i = i + 1 