
## REMEMBER THAT THIS FILE MUST NOT CONTAIN ANYTHING OTHER THAN YOUR
## FUNCTION DEFINITION, IMPORT STATEMENTS AND COMMENTS. You can use
## docstrings to document your functions, but a docstring should only
## be used inside a function definition, an then only at the very
## beginning of the function suite. Everywhere else you should use
## comments.

## Modify the following function definition so that it computes and
## returns the correct answer to the problem. (The statement "return 0"
## is just a placeholder: you should replace it.)


def approximate_integral(lower, upper, nterms):
    interval = (upper - lower) / nterms
    sum_area = 0
    for i in range(nterms):
        # area = ((abs(lower) + i*interval)**3 + (abs(lower) + (i+1)*interval)**3) / 2 * interval
        area = ((lower + i * interval) ** 3 + (lower + (i + 1) * interval) ** 3) / 2 * interval
        sum_area += area
    return sum_area



