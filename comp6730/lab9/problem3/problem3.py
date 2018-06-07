
## REMEMBER THAT THIS FILE MUST NOT CONTAIN ANYTHING OTHER THAN YOUR
## FUNCTION DEFINITION, IMPORT STATEMENTS AND COMMENTS. You can use
## docstrings to document your functions, but a docstring should only
## be used inside a function definition, an then only at the very
## beginning of the function suite. Everywhere else you should use
## comments.
import numpy as np
## Modify the following function definition so that it computes and
## returns the correct answer to the problem. (The return statement
## is just a placeholder: you should replace it.)


def moving_average(seq, wsize):
    """利用数组切片再求切片平均值的方法"""
    moving_list = []
    for i in range(len(seq) - wsize + 1):
        mean = np.mean(seq[i:i+wsize])
        moving_list.append(mean)
    return np.array(moving_list)
