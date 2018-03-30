#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:57:46 2018

@author: u6469050
"""

def print_grade(mark):
    if mark >= 80:
        print("High Distinction")
    else:
        if mark >= 70:
            print("Distinction")
        else:
            if mark >= 60:
                print("Credit")
            else:
                if mark >= 50:
                    print("Pass")
                else:
                    print("Fail")
