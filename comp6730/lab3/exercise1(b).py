#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:42:11 2018

@author: u6469050
"""

def print_grade(mark):
    if mark >= 80:
        print("High Distinction")
    elif mark >= 70:
            print("Distinction")
    elif mark >= 60:
        print("Credit")
    elif mark >= 50:
        print("Pass")
    else:
        print("Fail")
