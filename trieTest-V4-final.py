import numpy

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
    candidates_reader = open("dataset/candidates_After_Removing_Algorithm.txt", "r")

    blends = []
    candidates = []
    dictTrie = Trie()
    dictReverseTrie = Trie()
    # candidateTrie = Trie()

    for line in blends_reader:
        blend = line.split('\t')[0]
        blends.append(blend)

    for line in candidates_reader:
        candidates.append(line.split('\n')[0])

    for line in dicts_reader:
        dict = line.split('\n')[0]
        dictTrie[dict] = 0
        dictReverseTrie[dict[::-1]] = 1

    # end1 = datetime.datetime.now()
    # print("create list and trie need :" + str(end1 - start))

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


    # debug testing : getSuffixList("caceres")
    # print(getSuffixList("cabeza"))
    # print("prefix:")
    # print(getPrefixList('abcdef'))
    # print("suffix")
    # print(getSuffixList("abcd"))

    # '''
    dictectBlendList = []
    i = 0
    percent = 0
    for candidate in candidates:
        i += 1
        if i == 120 :
            i = 0
            percent += 1
            print("processing is done :" + str(percent) + "%")
        # canStartTime = datetime.datetime.now()
        prefixDict = {}
        suffixDict = {}
        combDict = {}
        prefixList = getPrefixList(candidate)
        suffixList = getSuffixList(candidate)

        # presuffixTime = datetime.datetime.now()
        # print("Get prefix and suffix need :")
        # print(presuffixTime - canStartTime)
        for prefix in prefixList:
            simjw = JaroWinkerSim.get_jaro_distance(prefix, candidate)
            prefixDict[prefix] = simjw

        for suffix in suffixList:
            simjw_suffix = JaroWinkerSimSuffix.get_jaro_distance_suffix(suffix, candidate)
            suffixDict[suffix] = simjw_suffix

        # JaroTime = datetime.datetime.now()
        # print("Get Jaro winker sim need :")
        # print(JaroTime - presuffixTime)
        # ranking the prefix and suffix dicts by value and then get top 5 String
        # prefixDictRanking = sorted(prefixDict.items(), key=lambda d:d[1], reverse = True)
        prefixDictTop5 = heapq.nlargest(10, prefixDict, key=prefixDict.get)
        suffixDictTop5 = heapq.nlargest(10, suffixDict, key=suffixDict.get)
        combList = []
        for prefix in prefixDictTop5:
            for suffix in suffixDictTop5:
                comb = prefix+suffix
                # remove some impossible combinations
                if len(comb)>2.5*len(candidate) or len(comb)<0.7*len(candidate):
                    continue
                combList.append(comb)
                # combDict[prefix,suffix] = prefix+suffix
        # combList = list(combDict.values())
        # print(candidate + ":")
        # print("pre:" + str(prefixDictTop5))
        # print("suf:" + str(suffixDictTop5))
        # print(combDict)
        # print("comblist len is " +str(len(combList)))
        combSimNormList = []
        for comb in combList:
                combSimNormList.append(LevenshteinSim.recursive_levenshtein(candidate,comb)/len(comb))
        if len(combSimNormList)!=0 and min(combSimNormList) < 0.8:
            dictectBlendList.append(candidate)
        # canEndTime = datetime.datetime.now()
        # print("One candidate need : " +str(canEndTime - canStartTime))
        # print("candidate is " + candidate)
        # print(combSimList)
    # print(dictectBlendList)
    # print("the number of blend words : " + str(len(dictectBlendList)))

    countBlend = 0
    trueBlends = []
    for blend in dictectBlendList:
        if blend in blends:
            trueBlends.append(blend)
            countBlend +=1
    # precision
    precision = round(countBlend / len(dictectBlendList),4)
    recall = round(countBlend / len(blends),4)

    print("precision\t:\t" + str(precision))
    print("recall\t:\t" + str(recall))

    trueBlendsArray = numpy.array(trueBlends)
    numpy.savetxt("result_data/tureBlendArray20190911-all-v1.txt", trueBlendsArray, fmt="%s")

    dictetBlendArray = numpy.array(dictectBlendList)
    numpy.savetxt("result_data/dictetBlendArray20190911-all-v1.txt", dictetBlendArray, fmt="%s")
    # '''
    end = datetime.datetime.now()
    print("the whole program needs " + str(end - start))
