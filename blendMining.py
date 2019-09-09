
import matplotlib.pyplot as plt
import os
import LevenshteinSim

'''
This python file aims to mine features and patterns about blend words using blends.txt
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
        print(str(i) + ":" + str(prefix_num_List.count(i)))
    plt_prefix = plt
    plt_prefix.title("Prefix Count")
    plt_prefix.xlabel("The number of same Prefix between blend and combination")
    plt_prefix.ylabel("Frequency")
    plt_prefix.bar(prefix_value_List, prefix_count_List,color="#87CEFA")
    plt_prefix.xticks(prefix_value_List)
    plt_prefix.savefig("figure/prefixCount.pdf")
    plt_prefix.show()

    # suffix count and figure
    suffix_value_List = []
    suffix_count_List = []
    for i in set(suffix_num_List):
        suffix_value_List.append(i)
        suffix_count_List.append(suffix_num_List.count(i))
        print(str(i) + ":" + str(suffix_num_List.count(i)))
    plt_suffix = plt
    plt_suffix.title("Suffix Count")
    plt_suffix.xlabel("The number of same suffix between blend and combination")
    plt_suffix.ylabel("Frequency")
    plt_suffix.bar(suffix_value_List, suffix_count_List,color="#87CEFA")
    plt_suffix.xticks(suffix_value_List)
    plt_suffix.savefig("figure/suffixCount.pdf")
    plt_suffix.show()

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
    # picCount_prefix_suffix()

    #Mining 2:
    # How much the Global Edit Distance between blends and their combinations?
    # getGED()











