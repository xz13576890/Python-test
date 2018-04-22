

def allbut(a_list, index):
    new_list = a_list.pop(index)


def choices(n,k):
    if k == 0 or k == n:
        return 1
    else:
        return choices(n-1, k) + choices(n-1, k-1)

