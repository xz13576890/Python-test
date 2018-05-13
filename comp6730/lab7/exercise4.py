def reverse_lookup(d, v):
    """
    查找字典d中是否含有value v，如有则返回第一个符合的key，
    若没有则报错
    :param d: 任意dict
    :param v: value
    :return: 包含v的key
    """
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('value does not appear in the dictionary')


def invert_dictionary(d):
    inverse_d = {}
    for item in d.items():
        key, value = item
        inverse_d[value] = key
    return inverse_d


def invert_dictionary1(d):
    """
    转置一个dict使其含有相同value的key成为一个list
    :param d:一个字典
    :return:转置了key和value的新字典
    """
    inverse_d = dict()
    for key in d:
        val = d[key]
        if val not in inverse_d:
            inverse_d[val] = [key]
        else:
            inverse_d[val].append(key)
    return inverse_d
