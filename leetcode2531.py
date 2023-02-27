# 2531. Make Number of Distinct Characters Equal

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        w1, w2 = Counter(word1), Counter(word2)
        
        for c1 in list(w1.keys()):
            for c2 in list(w2.keys()):
                cntw1, cntw2 = 0, 0
                w1[c1] -= 1
                w2[c2] -= 1
                w1[c2] += 1
                w2[c1] += 1
                
                if w1[c1] == 0:
                    del w1[c1]
                if w2[c2] == 0:
                    del w2[c2]
                
                if len(w1.keys()) == len(w2.keys()):
                    return True

                w1[c1] += 1
                w2[c2] += 1
                w1[c2] -= 1
                w2[c1] -= 1
                
                if w1[c2] == 0:
                    del w1[c2]
                if w2[c1] == 0:
                    del w2[c1]
                
        return False
            
