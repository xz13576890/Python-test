## COMP1730/6730 S1 2018 - Homework 5
## Due: 6pm, Sunday 22 April, 2018.

## uid: u6469050 - replace this with your uid number.

## The assignment can be done together in pairs, but not in a group of
## more than two students.
##
## If you work in a pair, both students must submit solution files, and
## both students must attend the following lab and answer the tutors
## questions. In this file, you must write a comment to say who you
## worked together with, like this:
##
## I worked together with NNNNNN (ANU id: NNNNNN).
##
## Both of you must be able to explain every part of your submitted
## solution. The tutor will choose who to address each question to, and
## only the student addressed may answer. It is not acceptable to divide
## the assignment up so that one student does half and the other student
## the other half.

## Modify the following function definition so that it computes and
## returns the correct answer to the homework problem. (The statement
## "return 0" is just a placeholder: you should of course modify it.)

'''
This function interpolate(x, y, x_test) input two sequences x and y and
a number x_test as parameters, x and y indicate the domain and range of 
a bijiective function y=f(x), x_test is a number between x[satrt:end], this
function interpolate(x, y, x_test) will return the correspond y(x_test) 
in the origonal function f=f(x)
'''


def interpolate(x, y, x_test):
    if x_test in x:  #if x_text belongs to x
        index_x_test = x.index(x_test)
        return y[index_x_test]  #just return y(x_text)
    else:
        index = 0
        x_above = 0
        while index < len(x):  
            if x[index] > x_test:  #find the position of x_test in x
                x_above = x[index]  #find x_above
                break
            else:
                index += 1
        x_below = x[index - 1]
        y_above = y[index]
        y_below = y[index -1]
        a = (y_above - y_below)/(x_above - x_below)  #  definition of a,b
        b = y_below - a * x_below
        y_x_test = a * x_test + b
        return y_x_test

## REMEMBER THAT THIS FILE (WHEN YOU SUBMIT IT) MUST NOT CONTAIN ANYTHING
## OTHER THAN YOUR FUNCTION DEFINITION AND COMMENTS. You can (and should)
## use docstrings to document your functions, but a docstring should only
## be used inside a function definition, an then only at the very beginning
## of the function suite. Everywhere else you should use comments.

## You may not include import statements in your submission.
