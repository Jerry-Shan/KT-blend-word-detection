import numpy

__author__ = 'Jinzhe-Shan - jinzhes@student.unimleb.edu.au'
'''
V2 Lastest update date : 2019-09-10
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
    dicts_reader = open("dataset/dict.txt", "r" )
    candidates_reader = open("dataset/candidates.txt", "r")
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
    # print(dictReverseTrie)
    # print(len(dictReverseTrie))
    # prefixList = dictReverseTrie.keys(prefix='yl')
    # print(prefixList)
    end1 = datetime.datetime.now()
    print("create list and trie need :")
    print(end1 - start)
    def getPrefixList(str):
        prefixList = []
        for i in range(len(str)):
            for j in dictTrie.keys(prefix = str[:i]):
                prefixList.append(j)
        return prefixList
    def getSuffixList(str):
        str_reverse = str[::-1]
        suffixList = []
        for i in range(1,len(str)):
            # print(str_reverse[:i])
            for j in dictReverseTrie.keys(prefix=str_reverse[0:i]):
                j_reverse = j[::-1]
                suffixList.append(j_reverse)
        return suffixList

    # print(getPrefixList("ajly"))
    # print(getSuffixList("ajly"))


    dictectBlendList = []
    for candidate in candidates:
        canTime = datetime.datetime.now()
        prefixDict = {}
        suffixDict = {}
        combDict = {}
        prefixList = getPrefixList(candidate)
        suffixList = getSuffixList(candidate)
        presuffixTime = datetime.datetime.now()
        # print("prefixList:")
        # print(prefixList)
        print("Get prefix and suffix need :")
        print(presuffixTime - canTime)
        for dict in prefixList:
            simjw = JaroWinkerSim.get_jaro_distance(dict, candidate)
            prefixDict[dict] = simjw

        for dict in suffixList:
            simjw_suffix = JaroWinkerSimSuffix.get_jaro_distance_suffix(dict, candidate)
            suffixDict[dict] = simjw_suffix

        JaroTime = datetime.datetime.now()
        print("Get Jaro winker sim need :")
        print(JaroTime - presuffixTime)
        # ranking the prefix and suffix dicts by value and then get top 5 String
        # prefixDictRanking = sorted(prefixDict.items(), key=lambda d:d[1], reverse = True)
        prefixDictTop5 = heapq.nlargest(5, prefixDict, key=prefixDict.get)
        suffixDictTop5 = heapq.nlargest(5, suffixDict, key=suffixDict.get)
        for prefix in prefixDictTop5:
            for suffix in suffixDictTop5:
                combDict[prefix,suffix] = prefix+suffix
        combList = list(combDict.values())
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
        canEndTime = datetime.datetime.now()
        print("One candidate need : ")
        print(canEndTime - canTime)
        # print("candidate is " + candidate)
        # print(combSimList)
    # print(dictectBlendList)
    print("the number of blend words : " + str(len(dictectBlendList)))
    dictetBlendArray = numpy.array(dictectBlendList)
    numpy.savetxt("dictetBlendArray.txt", dictetBlendArray, fmt="%s")
    end = datetime.datetime.now()
    print(end - start)