#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:15:40 2018

@author: u6469050
"""

'''
Create a list containing 100 elements that all have the same value, 
e.g. all are 1. Try to find three different approaches. 
Discuss your three alternatives with your neighbour - 
did you find the same three, or different ones?
'''
Q1=100*[1]

Q2=[1]
while len(Q2)<100:
    Q2.append(1)
 
a1=99*[1]
Q3=[1]
Q3.extend(a1)
print(Q3)
    
'''
Create a list of 100 integers whose value is the same as 
their index (position in the list) plus 1, that is, 
mylist[0] == 1, mylist[1] == 2, mylist[2] == 3, etc.
'''

mylsit=[x+1 for x in range(0,100)]
