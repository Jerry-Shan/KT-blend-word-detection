import numpy

__author__ = 'Jinzhe-Shan - jinzhes@student.unimleb.edu.au'
'''
Version Description
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

    blends_reader = open("dataset/testblends.txt", "r")
    detections_reader = open("result_data/dictetBlendArray20190910-v1.txt", "r")

    blends = []
    dictectBlendList = []
    for line in blends_reader:
        blend = line.split('\t')[0]
        blends.append(blend)

    for line in detections_reader:
        dictectBlendList.append(line.split("\n")[0])
    countBlend = 0
    true_blends = []
    for blend in dictectBlendList:
        if blend in blends:
            true_blends.append(blend)
            countBlend +=1
    print(true_blends)
    # precision & recall
    precision = round(countBlend / len(dictectBlendList),4)
    recall = round(countBlend / len(blends),4)

    print("precision\t:\t" + str(precision))
    print("recall\t:\t" + str(recall))

    # dictetBlendArray = numpy.array(dictectBlendList)
    # numpy.savetxt("result_data/dictetBlendArray20190910-v1.txt", dictetBlendArray, fmt="%s")
    # '''
    end = datetime.datetime.now()
    print("the whole program needs " + str(end - start))
