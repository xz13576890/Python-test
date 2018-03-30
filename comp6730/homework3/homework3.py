## COMP1730/6730 S1 2018 - Homework 3
## Due: 6:00pm Sunday 18 March, 2018.

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
def total_days(start_year, end_year):
    years = end_year - start_year
    check_years = 0
    leap_years = 0
    
    if 0 < years < 400:
        while check_years < years:
            if ((start_year + check_years) % 4 == 0 and (start_year + check_years) % 100 != 0) or (start_year + check_years) % 400  == 0 :
                leap_years = leap_years + 1
                check_years = check_years + 1
            check_years = check_years + 1
        return int(leap_years * 366 + (years - leap_years) * 365)
    
    if years >= 400:
        while check_years < years:
            if ((start_year + check_years) % 4 == 0 and (start_year + check_years) % 100 != 0) or (start_year + check_years) % 400 == 0 :
                leap_years = leap_years + 1
                check_years = check_years + 1
            check_years = check_years + 1
        return int(leap_years * 366 + (years - leap_years) * 365 - (years//400) * 3)
        
    else:    
        return "year input error!" 
        

## REMEMBER THAT THIS FILE (WHEN YOU SUBMIT IT) MUST NOT CONTAIN ANYTHING
## OTHER THAN YOUR FUNCTION DEFINITION AND COMMENTS. You can (and should)
## use docstrings to document your functions, but a docstring should only
## be used inside a function definition, and then only at the very beginning
## of the function suite. Everywhere else you should use comments.

## IF YOUR FILE CONTAINS THINGS THAT ARE NOT PART OF THE SPECIFICATION,
## YOU WILL RECEIVE A MARK OF ZERO.
