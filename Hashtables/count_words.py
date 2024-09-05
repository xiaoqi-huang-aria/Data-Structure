import random
from KVItem import KVItem
from DictionaryAsList import DictionaryAsDoubleList
from ChainHashtable import ChainHashtable


def main():
    #table = DictionaryAsDoubleList()
    table = ChainHashtable(7)
    file = open("count_words.txt", "r")

    for line in file:
        words = line.split()
        for word in words:
            if word in table:
                table[word] += 1
            else:
                table[word] = 1

    print(table)

    max_word = ""
    max_count = 0

    for key in table:
        if table[key] > max_count:
            max_count = table[key]
            max_word = key

    print('The most frequent word is', max_word)
    print('Its number of occurrences is', max_count)

main()