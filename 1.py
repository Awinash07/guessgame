# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 09:44:59 2020

@author: dell
"""
import sys
from random import randint
import sys
#generate a number 1-10
ans = randint(int(sys.argv[1]),int(sys.argv[2]))
#input from user?

#check that input is a number 1-10
while True:
    try:
        guess = int(input('guess a no 1-10:'))
        if 0<guess<11:
            if guess== ans:
                print("u r genius!")
            
        else:
            print("enter b/w 1-10")
    except ValueError:
        print("please enter a no")
        continue
