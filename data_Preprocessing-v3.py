__author__ = 'Jinzhe-Shan - jinzhes@student.unimleb.edu.au'
'''
Version Description

V3 
Testing the quality of data preprocesing on candicates by comparing with blends.txt

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

    candidates_reader_2 = open("dataset/candidates_Initial_Letter_is_C.txt", "r")
    candidates_2 = []

    blends_reader = open("dataset/testblends.txt","r")
    blends = []
    count = 0
    count_2 = 0
    for line in blends_reader:
        blend = line.split('\t')[0]
        blends.append(blend)

    for line in candidates_reader:
        candidate = line.split('\n')[0]
        if candidate in blends:
            count +=1
        candidates.append(candidates)

    for line in candidates_reader_2:
        candidate_2 = line.split('\n')[0]
        if candidate_2 in blends:
            count_2 +=1
        candidates_2.append(candidate_2)

    print("#blends included in blends.txt:" + str(count) + "/" + str(len(blends)))
    print("#blends in candidates_Initial_Letter_is_C.txt:" + str(count) + "/" + str(len(candidates)))
    print("#blends in candidates_Initial_Letter_is_C_After_Removing_Algorithm.txt:" + str(count_2) +"/" + str(len(candidates_2)))



    end = datetime.datetime.now()
    print("the whole program needs :" + str(end - start))
    # '''