## COMP1730/6730 S1 2018 - Homework 4
## Due date: 6pm, Sunday, 15 April, 2018.

## uid: u6469050 - replace this with your student id.

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
## "return 1" is just a placeholder: you should of course modify it.)


def max_relative_frequency(s):
    i = 0
    j = 0
    k = 0
    c = list()
    low = s.lower()  # all transform into lowercase
    while i < len(low):
        char = low[i]
        if 97 <= ord(char) <= 122:  # detect char from a~z
            c.append(low.count(char))  # pick all a~z numbers' count
        i = i + 1
    for char in low:
        if 97 <= ord(char) <= 122:
            j = j + 1  # count the a~z number
        else:
            k = k + 1  # count the non-a~z char number
    if k != len(low):
        c1 = max(c)  # count the highest repeated number
        return c1/j
    else:
        return 0

## REMEMBER THAT THIS FILE (WHEN YOU SUBMIT IT) MUST NOT CONTAIN ANYTHING
## OTHER THAN YOUR FUNCTION DEFINITION AND COMMENTS. You can (and should)
## use docstrings to document your functions, but a docstring should only
## be used inside a function definition, an then only at the very beginning
## of the function suite. Everywhere else you should use comments.

## YOU MAY NOT USE IMPORT STATEMENTS FOR THIS HOMEWORK.

## IF YOUR FILE DOES NOT SATISFY THESE REQUIREMENTS IT WILL NOT BE MARKED.
