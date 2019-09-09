# import os
import JaroWinkerSim
import LevenshteinSim

if __name__ == "__main__":
    simjw = JaroWinkerSim.get_jaro_distance("caet", "cart")
    simLev = LevenshteinSim.classic_levenshtein("caet", "cart")
    print(simjw,simLev)
