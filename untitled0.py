# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:49:46 2021

@author: Hp
"""

cube=lambda c:c*c*c
print(cube(5))


def cue(x):
    
    return x*x
print(cue(5))


a=[5,6,7,8]
b=filter(lambda j:j[0]==5,a)
print(list(b))


a=input("enter the words")
b=a[::-1]
if(a==b):
    print("string is palidrome")
else:
    print("string is not palidrome")
    
for i in range(0,51):
    pali=i[::-1]
    print(i)
