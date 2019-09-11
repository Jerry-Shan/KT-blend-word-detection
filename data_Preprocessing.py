__author__ = 'Jinzhe-Shan - jinzhes@student.unimleb.edu.au'
'''
Version Description
V1 Latest update date : 2019-09-10 17:00
Preprocessing candidates.txt and dict.txt to remove some candidate words because they are impossible as actual blend words

'''
import heapq
from pytrie import SortedStringTrie as Trie
import re
import numpy
import JaroWinkerSim
import JaroWinkerSimSuffix
import LevenshteinSim
import datetime

if __name__ == "__main__":
    # '''
    start = datetime.datetime.now()

    candidates_reader = open("dataset/candidates_Initial_Letter_is_C.txt", "r")
    candidates = []

    dicts_reader = open("dataset/dict.txt", "r")
    dictTrie = Trie()

    # create dictionary tree using 'pytrie' library
    for line in dicts_reader:
        dict = line.split('\n')[0]
        dictTrie[dict] = 0

    def getPrefixList(str):
        prefixList = []
        for i in range(1,len(dictTrie.longest_prefix(str))+1):
            for j in dictTrie.keys(prefix = str[0:i]):
                if abs(len(j) - len(str)) < 2:
                    prefixList.append(j)
        return list(set(prefixList))
    # '''

    # print(getPrefixList("abeaj"))
    '''
    Remove strategies:
        1. one letter repeats more than 3 times, such as 'storrrmmm', 'stoneeeeeeeee' and 'stuuuuuuuuuupidd'
        2. the length of word is less than 2, such as 'cz','ek'and 'oj'
        3. candidate has some words with their global edit distance less than 2,
        because it is more possible as spelling mistake rather than blend word
    '''
    # one letter repeats more than 3 times in a word
    rule1 = re.compile('([a-z])\\1{2,}')
    # result = rule1.findall('aahhh')
    # print(result)

    # '''
    removeList = []
    i = 0
    for line in candidates_reader:
        i += 1
        print(str(i))
        candidate = line.split('\n')[0]
        # print(rule1.findall(candidate))
        # print(candidate)
        if len(candidate)<3: #len(rule1.findall(candidate))!=0 or
            continue
        if len(rule1.findall(candidate))!=0:
            continue
        prefixList = getPrefixList(candidate)
        for prefix in prefixList:
            if LevenshteinSim.recursive_levenshtein(candidate, prefix) < 3:
                removeList.append(candidate)
                continue
        candidates.append(candidate)

    candidatesArray = numpy.array(candidates)
    numpy.savetxt("dataset/candidates_Initial_Letter_is_C_After_Removing_Algorithm.txt", candidatesArray, fmt="%s")
    print("remove words are : " +str(removeList))
    end = datetime.datetime.now()
    print("the whole program needs :" + str(end - start))
    # '''