def histogram(seq):
    """
    计算有序序列（list,string,etc)中每个元素出现次数
    :param seq:一个有序序列
    :return: 一个由（元素名：出现次数）组成的新字典
    """
    count = dict()
    for elem in seq:
        if elem not in count:
            count[elem] = 1
        else:
            count[elem] += 1
    return count

