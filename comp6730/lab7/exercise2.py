def histogram(seq):
    count = dict()
    for elem in seq:
        if elem not in count:
            count[elem] = 1
        else:
            count[elem] += 1
    return count

