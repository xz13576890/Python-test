
## REMEMBER THAT THIS FILE MUST NOT CONTAIN ANYTHING OTHER THAN YOUR
## FUNCTION DEFINITION, IMPORT STATEMENTS AND COMMENTS. You can use
## docstrings to document your functions, but a docstring should only
## be used inside a function definition, an then only at the very
## beginning of the function suite. Everywhere else you should use
## comments.

## Modify the following function definition so that it computes and
## returns the correct answer to the problem. (The return statement
## is just a placeholder: you should replace it.)


def unnest(alist):
    new_list = []
    for elem in alist:
        if isinstance(elem, list):
            # recursive way
            new_list.extend(unnest(elem))
        else:
            new_list.append(elem)
    return new_list


