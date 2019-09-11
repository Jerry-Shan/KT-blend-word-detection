import numpy

__author__ = 'Jinzhe-Shan - jinzhes@student.unimleb.edu.au'
'''
V3 Lastes update date : 2019-09-10 15:00
Using pure trie firstly, but it has some trouble when I want to combine the prefix and suffix to combination
and then caculate their Global Edit Distance with candidate.
Because if only using trie, I will get numerous prefix and suffix, the algorithm complexity of combination prefix
and suffix is len(prefixList) * len(suffixList). 

V2 Lastest update date : 2019-09-10 1:00
Add the getSuffixList(str) method to get whole words with the same suffix.
But the efficiency is still low. So I consider to remove jaro and global edit distance firstly.

V1 Latest update date: 2019-09-09
This method aims to create a prefix tree using pytrie library and find words which have the same prefix
After using prefix tree, the cumputing efficiency of coding is much faster

'''
import heapq
from pytrie import SortedStringTrie as Trie
import JaroWinkerSim
import JaroWinkerSimSuffix
import LevenshteinSim
import datetime

if __name__ == "__main__":
    start = datetime.datetime.now()
    print("KT assignment 1 starts from " + str(start))
    dicts_reader = open("dataset/testdict.txt", "r" )
    candidates_reader = open("dataset/candidates_Initial_Letter_is_C.txt", "r")
    dicts = {}
    candidates = []

    dictTrie = Trie()
    dictReverseTrie = Trie()
    candidateTrie = Trie()
    for line in dicts_reader:
        dict = line.split('\n')[0]
        dictTrie[dict] = 0
        dictReverseTrie[dict[::-1]] = 1

    for line in candidates_reader:
        candidates.append(line.split('\n')[0])
        candidateTrie[line.split('\n')[0]] = 0

    print ("longest prefix string of abercrombie is " + str(dictTrie.longest_prefix("abercrombie")))
    print("all prefix list:")
    prefixList = dictTrie.keys(prefix=dictTrie.longest_prefix("abercrombie"))
    print(prefixList)

    # print(dictReverseTrie)
    # print(len(dictReverseTrie))
    # prefixList = dictReverseTrie.keys(prefix='yl')
    # print(prefixList)
    '''

    end1 = datetime.datetime.now()
    # print("create list and trie need :")
    # print(end1 - start)
    def getSuffixList(str):
        suffixList = []
        for j in dictReverseTrie.keys(prefix=dictReverseTrie.longest_prefix(str)):
            j_reverse = j[::-1]
            suffixList.append(j_reverse)
        return suffixList

    # print(getPrefixList("ajly"))
    # print(getSuffixList("ajly"))


    dictectBlendList = []
    i = 0
    for candidate in candidates:
        i += 1
        print(str(i) + "/" + str(len(candidates)))
        canTime = datetime.datetime.now()
        prefixDict = {}
        suffixDict = {}
        combDict = {}
        prefixList = dictTrie.keys(prefix = dictTrie.longest_prefix(candidate))
        suffixList = getSuffixList(candidate)
        # presuffixTime = datetime.datetime.now()
        # print("candidate : " + candidate)
        # print("prefixList len:" + str(len(prefixList)))
        # print(prefixList)
        # print("suffixList len:" + str(len(suffixList)))
        # print(suffixList)
        # print("Get prefix and suffix need :")
        # print(presuffixTime - canTime)

        combList = []
        for prefix in prefixList:
            for suffix in suffixList:
                comb = prefix + suffix
                if len(comb) > len(candidate) + 10 or len(comb) < len(candidate):
                    continue
                combList.append(prefix+suffix)
        # print(candidate + ":")
        # print("pre:" + str(prefixDictTop5))
        # print("suf:" + str(suffixDictTop5))
        # print(combDict)
        # print(comb)
        # combSimList = []
        combSimNormList = []
        for comb in combList:
            combSimNormList.append(LevenshteinSim.recursive_levenshtein(candidate,comb)/len(comb))
                # combSimList.append(LevenshteinSim.recursive_levenshtein(candidate,comb))
        if len(combSimNormList)!=0 and min(combSimNormList) < 0.5:
            dictectBlendList.append(candidate)
        # canEndTime = datetime.datetime.now()
        # print("One candidate need : ")
        # print(canEndTime - canTime)
        # print("candidate is " + candidate)
        # print(combSimList)
    # print(dictectBlendList)
    print("the number of blend words : " + str(len(dictectBlendList)))
    dictetBlendArray = numpy.array(dictectBlendList)
    numpy.savetxt("dictetBlendArray.txt", dictetBlendArray, fmt="%s")
    end = datetime.datetime.now()
    print(end - start)
    '''