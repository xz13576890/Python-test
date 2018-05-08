def funA(a, i):
    try:
        return a[i] + i
    except TypeError:
        print("Caught TypeError in funA")
    except IndexError:
        print("Caught IndexError in funA")
    return 0


def funB(a, i):
    try:
        i = funA(a, i)
        return a[i]
    except TypeError:
        print("Caught TypeError in funB")
    except IndexError:
        print("Caught IndexError in funB")
    return 0

def sorted_find(x, slist):
    if slist[-1] <= x:
        return slist[-1]
    lower = 0
    upper = len(slist) - 1
    while (upper - lower) > 1:
        middle = (lower + upper) // 2
        if slist[middle] <= x:
            lower = middle
        else:
            upper = middle
    return slist[lower]


def set_less_than(A, B):
    #Boolean flag
    good = False
    for elem in A:
        for elem2 in B:
            print(elem,elem2)
            try:
                if elem < elem2:
                    good = True
            except TypeError:
                print('Different types cannot be compared!')
        if not good:
            return False
    return good