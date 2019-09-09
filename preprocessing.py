import heapq
import operator
import os
import JaroWinkerSim

if __name__ == "__main__":
    # blend = np.array()
    dicts_reader = open("dataset/testdict.txt", "r" )
    candidates_reader = open("dataset/testcandidates.txt", "r" )
    dicts = []
    candidates = []
    for line in dicts_reader:
        dicts.append(line.split('\n')[0])
    for line in candidates_reader:
        candidates.append(line.split('\n')[0])

    # print(dicts)
    # print(candidates)

    comb = {}

    for candidate in candidates:
        simDict = {}
        sim = []
        for dict in dicts:
            simjw = JaroWinkerSim.get_jaro_distance(dict, candidate)
            sim.append(simjw)
            simDict[dict] = simjw
        print(simDict)
        # ranking the sim dict by value and then get top 5
        # simDictRanking = sorted(simDict.items(), key=lambda d:d[1], reverse = True)
        simDictTop5 = heapq.nlargest(5, simDict, key=simDict.get)
        print(simDictTop5)

        matchIndex = sim.index(max(sim))
        matchWord  = dicts[matchIndex]
        comb[candidate,matchWord] = max(sim)
        # print(candidate+" is the most similar with "+matchWord+ " the similirity is "+ str(max(sim)))
    print(comb)
