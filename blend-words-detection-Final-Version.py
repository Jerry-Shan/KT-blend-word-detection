__author__ = 'Jinzhe-Shan - jinzhes@student.unimleb.edu.au'
'''
Version Description

V4.1 Latest update date : 2019-09-11 1:00 
Testing all candidates and dicts using 2 hours and 45 mins.
precision is 1.3% 
recall is 62%

V4 Latest update date : 2019-09-10 16:00
Using codes based on trie-Test-V2
Testing testblend.txt and testcandidate.txt which includes words with initial letter 'C' 
Adding some strategies (data_Preprocessing.py)to remove candicate words because they are impossible as blend words 

V3 Latest update date : 2019-09-10 15:00
Using pure trie firstly, but it has some trouble when I want to combine the prefix and suffix to combination
and then calculate their Global Edit Distance with candidate.
Because if only using trie, I will get numerous prefix and suffix, the algorithm complexity of combination prefix
and suffix is len(prefixList) * len(suffixList). 

V2 Latest update date : 2019-09-10 1:00
Add the getSuffixList(str) method to get whole words with the same suffix.
But the efficiency is still low. So I consider to remove jaro and global edit distance firstly.

V1 Latest update date: 2019-09-09
This method aims to create a prefix tree using pytrie library and find words which have the same prefix
After using prefix tree, the cumputing efficiency of coding is much faster

'''
import heapq
import numpy
from pytrie import SortedStringTrie as Trie
import JaroWinkerSim
import JaroWinkerSimSuffix
import LevenshteinSim
import datetime

if __name__ == "__main__":
    start = datetime.datetime.now()
    print("KT assignment 1 starts from " + str(start))

    blends_reader = open("dataset/blends.txt","r")
    dicts_reader = open("dataset/dict_removing_algorithm.txt", "r" )
    candidates_reader = open("dataset/candidates_After_Removing_Algorithm-upperHalf.txt", "r")

    blends = []
    candidates = []
    dictTrie = Trie()
    dictReverseTrie = Trie()

    for line in blends_reader:
        blend = line.split('\t')[0]
        blends.append(blend)

    for line in candidates_reader:
        candidates.append(line.split('\n')[0])

    # create prefix dict tree and suffix dict tree
    for line in dicts_reader:
        dict = line.split('\n')[0]
        dictTrie[dict] = 0
        dictReverseTrie[dict[::-1]] = 1

    # get prefix and suffix
    def getPrefixList(str):
        prefixList = []
        if dictTrie.longest_prefix(str, default=-1) != -1:
            for i in range(1,len(dictTrie.longest_prefix(str))+1):
                for j in dictTrie.keys(prefix = str[0:i]):
                    prefixList.append(j)
            return list(set(prefixList))
        else:
            return str
    def getSuffixList(str):
        str_reverse = str[::-1]
        suffixList = []
        if dictReverseTrie.longest_prefix(str_reverse,default=-1) !=-1:
            for i in range(1,len(dictReverseTrie.longest_prefix(str_reverse))+1):
                # print(str_reverse[:i])
                for j in dictReverseTrie.keys(prefix=str_reverse[0:i]):
                    j_reverse = j[::-1]
                    suffixList.append(j_reverse)
            return suffixList
        else:
            return str

    dictectBlendList = []

    # the main structure of Blend Word Detection Algorithm
    for candidate in candidates:
        # get prefix and suffix
        prefixDict = {}
        suffixDict = {}
        combDict = {}
        prefixList = getPrefixList(candidate)
        suffixList = getSuffixList(candidate)

        # culcalate the jaro-winker similarity
        for prefix in prefixList:
            simjw = JaroWinkerSim.get_jaro_distance(prefix, candidate)
            prefixDict[prefix] = simjw

        for suffix in suffixList:
            simjw_suffix = JaroWinkerSimSuffix.get_jaro_distance_suffix(suffix, candidate)
            suffixDict[suffix] = simjw_suffix

        # get top 10 prefix words and suffix words and combine them to 100 combined strings
        prefixDictTop10 = heapq.nlargest(10, prefixDict, key=prefixDict.get)
        suffixDictTop10 = heapq.nlargest(10, suffixDict, key=suffixDict.get)
        combList = []
        for prefix in prefixDictTop10:
            for suffix in suffixDictTop10:
                comb = prefix+suffix
                # remove some impossible combinations
                if len(comb)>2.5*len(candidate) or len(comb)<0.6*len(candidate):
                    continue
                combList.append(comb)

        # Detection whether a candidate is a blend word or not
        combSimNormList = []
        for comb in combList:
                combSimNormList.append(LevenshteinSim.recursive_levenshtein(candidate,comb)/len(comb))
        if len(combSimNormList)!=0 and min(combSimNormList) < 0.6:
            dictectBlendList.append(candidate)

    countBlend = 0
    trueBlends = []
    for blend in dictectBlendList:
        if blend in blends:
            trueBlends.append(blend)
            countBlend +=1

    # precision recall
    precision = round(countBlend / len(dictectBlendList),4)
    recall = round(countBlend / len(blends),4)

    print("precision\t:\t" + str(precision))
    print("recall\t:\t" + str(recall))

    trueBlendsArray = numpy.array(trueBlends)
    numpy.savetxt("result_data/tureBlendArray20190912-all-2.txt", trueBlendsArray, fmt="%s")

    dictetBlendArray = numpy.array(dictectBlendList)
    numpy.savetxt("result_data/dictetBlendArray20190912-all-2.txt", dictetBlendArray, fmt="%s")
    # '''
    end = datetime.datetime.now()
    print("the whole program needs " + str(end - start))
