
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import LevenshteinSim

'''
This python file aims to mine features and patterns about blend words using blends.txt

# V3 Latest update date : 2019-09-11 
Adding length of blend words bar chart.

# V2 Global Edit Distance (GED) and GED Normalization analysis and draw CDF picture to 
determine the parameter for blend word detection algorithm 

# V1 prefix and suffix analysis 

'''

def get_diff_index_suffix(first, second):
    if first == second:
        return -1

    if not first or not second:
        return 0

    max_len = min(len(first), len(second))
    for i in range(1, max_len+1):
        if not first[-i] == second[-i]:
            return i - 1

    return max_len

def get_diff_index(first, second):
    if first == second:
        return -1

    if not first or not second:
        return 0

    max_len = min(len(first), len(second))
    for i in range(0, max_len):
        if not first[i] == second[i]:
            return i

    return max_len

def picCount_prefix_suffix():
    # prefix count and figure
    prefix_value_List = []
    prefix_count_List = []
    for i in set(prefix_num_List):
        prefix_value_List.append(i)
        prefix_count_List.append(prefix_num_List.count(i))
        # print(str(i) + ":" + str(prefix_num_List.count(i)))
    plt_prefix = plt
    plt_prefix.figure(figsize=(12, 8))
    # plt_prefix.title("Prefix Count")
    plt_prefix.xlabel("The number of same Prefix",fontsize = 30)
    plt_prefix.ylabel("Frequency",fontsize = 30)
    plt_prefix.bar(prefix_value_List, prefix_count_List,color="#87CEFA")
    plt_prefix.xticks(prefix_value_List,fontsize = 20)
    plt_prefix.yticks(fontsize = 20)
    plt_prefix.savefig("figure/prefixCount.png")
    plt_prefix.savefig("figure/prefixCount.pdf")
    plt_prefix.savefig("figure/prefixCount.eps")
    plt_prefix.show()

    # suffix count and figure
    suffix_value_List = []
    suffix_count_List = []
    for i in set(suffix_num_List):
        suffix_value_List.append(i)
        suffix_count_List.append(suffix_num_List.count(i))
        print(str(i) + ":" + str(suffix_num_List.count(i)))
    plt_suffix = plt
    plt_suffix.figure(figsize=(12, 8))
    # plt_suffix.title("Suffix Count")
    plt_suffix.xlabel("The number of same suffix",fontsize = 30)
    plt_suffix.ylabel("Frequency",fontsize = 30)
    plt_suffix.bar(suffix_value_List, suffix_count_List,color="#87CEFA")
    plt_suffix.xticks(suffix_value_List,fontsize = 20)
    plt_suffix.yticks(fontsize = 20)
    plt_suffix.savefig("figure/suffixCount.png")
    plt_suffix.savefig("figure/suffixCount.pdf")
    plt_suffix.savefig("figure/suffixCount.eps")
    plt_suffix.show()

    '''
    def getGED():
        gedFile = open("data_mining/ged_blend.csv", "a+")
        gedFile.write("blend" + "," + "ged" + "," + "gedNormalization" + "\n")
        gedList = []
        gedNormList = []
        for i in range(len(blendsList)):
            ged = LevenshteinSim.wf_levenshtein(blendsList[i], combinationsList[i])  # wf_levenshtein
            gedNormalization = ged / len(combinationsList[i])
            print(i, blendsList[i], ged, gedNormalization)
            gedFile.write(str(blendsList[i]) + "," + str(ged) + "," + str(gedNormalization) + "\n")
            gedList.append(ged)
            gedNormList.append(gedNormalization)
        gedFile.write(
            "average" + "," + str(sum(gedList) / len(gedList)) + "," + str(sum(gedNormList) / len(gedNormList)) + "\n")
        print("Average GED Normalization : " + str(sum(gedNormList) / len(gedNormList)))
        print("Max GED Normalization : " + str(max(gedNormList)))



def analizeGED():
    # draw CDF picture about GED and GED Normolization
    fig = plt.figure(figsize=(12, 8))
    plt.grid()
    # ax1 = fig.add_subplot(1, 1, 1)
    # plt.title('GED CDF')
    plt.xlim(0, 15) # for GED
    # plt.xlim(0, 1) # for GED Normalization
    plt.xticks(fontsize=30, rotation=0)
    plt.yticks(fontsize=30, rotation=0)
    plt.xlabel('GED', fontsize=30)
    # plt.xlabel('GED Normalization', fontsize=30)
    plt.ylabel('CDF', fontsize=30)

    df = pd.read_csv("data_mining\ged_blend_v2_average.csv")
    # GED
    ged = df['ged'].values
    sorted_ged = np.sort(ged)
    yvals = np.arange(len(sorted_ged)) / float(len(sorted_ged) - 1)
    plt.plot(sorted_ged, yvals, linewidth=3, color='#0C5DA5')

    #GED Normalization
    # gedNorm = df['gedNormalization'].values
    # sorted_gedNorm = np.sort(gedNorm)
    # yvals = np.arange(len(sorted_gedNorm)) / float(len(sorted_gedNorm) - 1)
    # plt.plot(sorted_gedNorm, yvals, linewidth=3, color='#0C5DA5')

    fig.savefig('figure/getCDF.png')
    # fig.savefig('figure/getCDF.eps')
    # fig.savefig('figure/getCDF.pdf')
    plt.show()
    print('GED CDF picture is saving')
    plt.close(1)

def getLength():
    df = pd.read_csv("data_mining\ged_blend_v2_average.csv")
    blend = df['blend'].values
    # print(blend)
    lenList = []
    lenList_Count = []
    for i in blend:
        lenList.append(len(i))
    lenList_Value = list(set(lenList))
    print(lenList_Value)
    for value in lenList_Value:
        count = lenList.count(value)
        print("len : count" + str(value) + str(count))
        lenList_Count.append(count)

    plt_length = plt
    plt_length.figure(figsize=(12, 8))
    # plt_suffix.title("Blend word Length Count")
    plt_length.xlabel("Blend Word Length",fontsize = 30)
    plt_length.ylabel("Frequency",fontsize = 30)
    plt_length.bar(lenList_Value, lenList_Count,color="#87CEFA")
    plt.yticks(fontsize=20, rotation=0)
    plt_length.xticks(range(3,16),fontsize=20)
    plt_length.savefig("figure/lengthCount.png")
    plt_length.savefig("figure/lengthCount.pdf")
    plt_length.savefig("figure/lengthCount.eps")
    plt_length.show()
'''


if __name__ == "__main__":
     blends_reader = open("dataset/blends.txt","r")
     blendsList = []
     comb_1List = []
     comb_2List = []
     combinationsList = [] # comb1 + comb2
     blends_combList = []
     prefix_num_List = []
     suffix_num_List = []
     for line in blends_reader:
         tempList = list(line.split('\t'))
         blends_combList.append(tempList)
         blend = tempList[0]
         comb_1 = tempList[1]
         comb_2 = tempList[2].split("\n")[0]
         blendsList.append(blend)
         comb_1List.append(comb_1)
         comb_2List.append(comb_2)
         combinationsList.append(comb_1+comb_2)
         # How many same prefix and suffix letters in blends ?
         prefix_num_List.append(get_diff_index(blend,comb_1))
         suffix_num_List.append(get_diff_index_suffix(blend,comb_2))

         # print(tempList)
         # print(comb_2)
     print(blendsList)
     # Mining 1 :
     # How many same prefix and suffix letters in blends ?
     picCount_prefix_suffix()


    # '''
    #  #Mining 2:
    #  # How much the Global Edit Distance between blends and their combinations?
    #  # getGED()
    #  analizeGED()
    #  getLength()
    # '''











