#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 00:27:07 2018

@author: u6469050
"""
def do_Twice(func,arg):
    func(arg)
    func(arg)
    
def print_spam():
    print("spam")
    
def print_Twice(bruce):
    print(bruce)
    print(bruce)

#do_Twice(print_spam)


#do_Twice(print_Twice,"spam")
    
def do_Four(f,G): #-----(func,arg) is ok too,all are local variables!
    do_Twice(f,G)
    do_Twice(f,G)
    
do_Four(print_Twice,"spam")

    