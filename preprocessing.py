import heapq
import JaroWinkerSim
import JaroWinkerSimSuffix
import LevenshteinSim

if __name__ == "__main__":
    # blend = np.array()
    dicts_reader = open("dataset/testdict.txt", "r" )
    candidates_reader = open("dataset/candidates_Initial_Letter_is_C.txt", "r" )

    dicts = []
    candidates = []
    for line in dicts_reader:
        dicts.append(line.split('\n')[0])
    for line in candidates_reader:
        candidates.append(line.split('\n')[0])

    for candidate in candidates:
        prefixDict = {}
        suffixDict = {}
        combDict = {}
        for dict in dicts:
            simjw = JaroWinkerSim.get_jaro_distance(dict, candidate)
            simjw_suffix = JaroWinkerSimSuffix.get_jaro_distance_suffix(dict, candidate)
            prefixDict[dict] = simjw
            suffixDict[dict] = simjw_suffix
        # ranking the prefix and suffix dicts by value and then get top 5 String
        # prefixDictRanking = sorted(prefixDict.items(), key=lambda d:d[1], reverse = True)
        prefixDictTop5 = heapq.nlargest(5, prefixDict, key=prefixDict.get)
        suffixDictTop5 = heapq.nlargest(5, suffixDict, key=suffixDict.get)
        # for prefix in prefixDictTop5:
        #     for suffix in suffixDictTop5:
        #         combDict[prefix,suffix] = prefix+suffix
        # combList = list(combDict.values())
        print(candidate + ":")
        print("pre:" + str(prefixDictTop5))
        print("suf:" + str(suffixDictTop5))
        # print(combDict)
        # print(comb)
        # combSimList = []
        # for comb in combList:
        #         combSimList.append(LevenshteinSim.classic_levenshtein(candidate,comb)/len(comb))
        # print("candidate is " + candidate)
        # print(combSimList)

