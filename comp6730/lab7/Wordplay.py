import histogram


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
    return print(most_frequent_list)


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


# word_frequency_wordlist(10)
find_triple_double()



