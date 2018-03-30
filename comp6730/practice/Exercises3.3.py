#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 00:27:07 2018

@author: u6469050
"""
#print("+","-"*4,"+","-"*4,"+")
#print("|"," "*4,"|"," "*4,"|")
"""
def print_Quartic():
    print("|         |         |")    
    print("|         |         |")  
    print("|         |         |")  
    print("|         |         |")  

print("+ - - - - + - - - - +")
print_Quartic()
print("+ - - - - + - - - - +")
print_Quartic()    
print("+ - - - - + - - - - +")

"""
#*******************************3.3.1
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

#print_grid()

#***************************************3.3.2

def do_quartic(f):
    f()
    f()
    f()
    f()

def print_beam4():
    do_quartic(print_beam)
    print("+")
    
def print_post4():
    do_quartic(print_post)
    print("|")
    
def print_row4():
    print_beam4()
    do_quartic(print_post4)

def print_grid4():
    do_quartic(print_row4)
    print_beam4()

print_grid4()
    
    










  