def invert_dictionary(d):
    inverse_d = {}
    for item in d.items():
        key,value = item
        inverse_d[value]=key
    return inverse_d

def invert_dictionary1(d):
    inverse_d = {}
    for item in d.items():
        key,value = item
        if key == value:
            inverse_d[value]=key
    return inverse_d