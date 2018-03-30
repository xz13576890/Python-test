#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:42:11 2018

@author: u6469050
"""

def median(a,b,c):
    if a < b < c or c < b < a:
        return b
    elif b < a < c or c < a < b:
        return a
    elif a < c < b or b < c < a:
        return c
    else:
        return "error!"
        
        