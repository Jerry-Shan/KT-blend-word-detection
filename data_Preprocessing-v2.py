__author__ = 'Jinzhe-Shan - jinzhes@student.unimleb.edu.au'
'''
Version Description

V2 Latest update date : 2019-09-10 18:00
Processing the removeWord.txt

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

    candidates_reader = open("dataset/candidates_Initial_Letter_is_C_After_Removing_Algorithm.txt", "r")
    candidates = []

    # removeList = []
    removeReader = open("data_mining/removeWord.txt")
    removeList = removeReader.readline().split(", ")
    removeList = list(set(removeList))
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
    i = 0
    for line in candidates_reader:
        i += 1
        print(str(i))
        candidate = line.split('\n')[0]
        # print(rule1.findall(candidate))
        # print(candidate)
        if len(candidate)<3 or len(candidate)>15:
            continue
        if len(rule1.findall(candidate))!=0:
            continue
        # prefixList = getPrefixList(candidate)
        # for prefix in prefixList:
        #     if LevenshteinSim.recursive_levenshtein(candidate, prefix) < 3:
        #         removeList.append(candidate)
        #         continue
        if candidate in removeList:
            continue
        candidates.append(candidate)

    removeWordArray = numpy.array(removeList)
    candidatesArray = numpy.array(candidates)
    numpy.savetxt("dataset/testcandidatesArray-v2.txt", candidatesArray, fmt="%s")
    numpy.savetxt("data_mining/removeWordArray.txt", removeWordArray, fmt="%s")

    print("remove words are : " +str(removeList))
    end = datetime.datetime.now()
    print("the whole program needs :" + str(end - start))
    # '''