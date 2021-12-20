# -*- coding: utf-8 -*-
"""
An easy FizzBuzz programe

@author: 44741
"""
#Input the integer
i = int(input("Input an integer:"))
#Set up number 1, not 0
a = 1
for a in range(1,i+1):
    #First check 15
    if a % 15 == 0:
        print ('FizzBuzz')
    #If not, check 5 and 3
    elif a % 5 == 0:
        print ('Buzz')
    elif a % 3 == 0:
        print ('Fizz')
    #Otherwise just print the number
    else:
        print(a)
