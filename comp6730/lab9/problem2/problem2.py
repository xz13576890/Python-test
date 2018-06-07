
## REMEMBER THAT THIS FILE MUST NOT CONTAIN ANYTHING OTHER THAN YOUR
## FUNCTION DEFINITION, IMPORT STATEMENTS AND COMMENTS. You can use
## docstrings to document your functions, but a docstring should only
## be used inside a function definition, an then only at the very
## beginning of the function suite. Everywhere else you should use
## comments.

## Modify the following function definition so that it computes and
## returns the correct answer to the problem. (The statement "return {}"
## is just a placeholder: you should replace it.)


def count_dict_difference(A, B):
    """充分运用集合的交集，差集原理"""
    a_keys_set = set(A.keys())
    b_keys_set = set(B.keys())
    dict_diff = dict()
    a_and_b_keys_set = a_keys_set & b_keys_set
    a_minus_b_keys_set = a_keys_set - b_keys_set
    if a_and_b_keys_set != {}:
        for elem1 in a_and_b_keys_set:
            n1 = A[elem1] - B[elem1]
            if n1 > 0:
                dict_diff[elem1] = n1
    if a_minus_b_keys_set != {}:
        for elem2 in a_minus_b_keys_set:
            dict_diff[elem2] = A[elem2]
    return dict_diff
