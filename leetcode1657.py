# 1657. Determine if Two Strings Are Close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for s in word1:
            d1[s] += 1
        for s in word2:
            d2[s] += 1
        
        return d1.keys() == d2.keys() and sorted(d1.values()) == sorted(d2.values())
