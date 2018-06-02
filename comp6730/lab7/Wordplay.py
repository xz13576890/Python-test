

def word_frequency_wordlist(number):
    """
    返回wordstring.txt文件中number数量个最频繁的词汇长度组成的list
    :param number:int
    :return:list
    """
    fileobj = open("wordstring.txt", 'r')
    word_list = fileobj.readlines()
    # 将每个词的长度组成一个集合
    wordlen_set = set(len(word) for word in word_list)
    most_frequent_list = []
    while number > 0:
        most_frequent = max(wordlen_set)
        most_frequent_list.append(most_frequent)
        wordlen_set.remove(most_frequent)
        number -= 1
    fileobj.close()
    return most_frequent_list


def is_triple_double(word):
    """
    Tests if a word contains three consecutive double letters
    :param word: string
    :return:  bool
    """
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('wordstring.txt')
    for line in fin:
        word = line.strip()  # 用于去除字符串首尾指定的字符，默认为空格
        if is_triple_double(word):
            print(word)
    fin.close()


def bi_gram_frequency(number):
    """目标文件中包含前number个最常见bi-gram"""
    fin = open("wordstring.txt")
    count = dict()
    frequency_list = []
    for line in fin:
        word = line.strip()
        i = 0
        while i+2 <= len(word):
            elem = word[i:i+2]
            if elem not in count:
                count[elem] = 1
            else:
                count[elem] += 1
            i += 1
    while number > 0:
        most_frequent_bi_gram = max(count, key=lambda k: count[k])  # lambda 表达式和max函数结合
        frequency_list.append(most_frequent_bi_gram)
        del count[most_frequent_bi_gram]
        number -= 1
    fin.close()
    print(frequency_list)


def bi_gram_alphabet():
    """26个字母构成的26*26个bi-gram组合中有多少不包含在目标文件中"""
    fin = open("wordstring.txt")
    count = dict()
    alphabet_list = [chr(i) for i in range(97, 123)]
    alphabet_bi_gram = []
    bi_grams_not_in_number = 0
    bi_grams_not_in_number_list = []
    for line in fin:
        word = line.strip()
        i = 0
        while i+2 <= len(word):
            elem = word[i:i+2]
            if elem not in count:
                count[elem] = 1
            else:
                count[elem] += 1
            i += 1
    for char in alphabet_list:
        for i in range(len(alphabet_list)):
            alphabet_bi_gram.append(char+alphabet_list[i])
    for elem in alphabet_bi_gram:
        if elem not in count:
            bi_grams_not_in_number += 1
            bi_grams_not_in_number_list.append(elem)
    fin.close()
    print(bi_grams_not_in_number)
    print(bi_grams_not_in_number_list)


def repeated_bi_gram():
    """目标文件中有多少单词具有重复的bi-gram"""
    fin = open("wordstring.txt")
    count = []
    count_repeated_bi_gram = 0
    for line in fin:
        word = line.strip()
        i = 0
        while i+2 <= len(word):
            elem = word[i:i+2]
            if elem not in count:
                count.append(elem)
            else:
                count_repeated_bi_gram += 1
                count.clear()
                break
            i += 1
    fin.close()
    print(count_repeated_bi_gram)


def highest_number_of_repeated_bi_gram():
    """wordstring.txt中拥有重复bi-gram的最大数，以及哪一个单词拥有该最大重复数"""
    fin = open("wordstring.txt")
    count = []
    repeated_word = dict()
    for line in fin:
        word = line.strip()
        count_repeated_bi_gram = 0
        i = 0
        while i+2 <= len(word):
            elem = word[i:i+2]
            if elem not in count:
                count.append(elem)
            else:
                count_repeated_bi_gram += 1
            i += 1
        if count_repeated_bi_gram > 0:
            repeated_word[word] = count_repeated_bi_gram
        count.clear()
    fin.close()
    print(max(repeated_word.values()))
    print(max(repeated_word, key=lambda k: repeated_word[k]))


if __name__ == '__main__':
    # word_frequency_wordlist(10)
    # find_triple_double()
    # bi_gram_frequency(10)
    # bi_gram_alphabet()
    # repeated_bi_gram()
    # highest_number_of_repeated_bi_gram()
    pass



