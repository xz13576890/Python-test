
## REMEMBER THAT THIS FILE MUST NOT CONTAIN ANYTHING OTHER THAN YOUR
## FUNCTION DEFINITION, IMPORT STATEMENTS AND COMMENTS. You can use
## docstrings to document your functions, but a docstring should only
## be used inside a function definition, an then only at the very
## beginning of the function suite. Everywhere else you should use
## comments.

## Modify the following function definition so that it computes and
## returns the correct answer to the problem. (The statement "return 0"
## is just a placeholder: you should replace it.)


def digit_sum(number):
    numstr = str(number)
    sum_digit = 0
    for char in numstr:
        sum_digit += int(char)
    return sum_digit
