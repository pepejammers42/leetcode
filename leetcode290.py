# Leetcode 290

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()
        if len(words) != len(pattern): return False

        d1, d2 = {}, {}
        
        for i in range(len(pattern)):
            if pattern[i] not in d2:
                d2[pattern[i]] = words[i]
            elif d2[pattern[i]] != words[i]:
                return False

            if words[i] not in d1:
                d1[words[i]] = pattern[i]
            elif d1[words[i]] != pattern[i]:
                return False
        return True
