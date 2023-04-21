class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        s = ""
        
        while l < len(word1) and r < len(word2):
            s += word1[l] + word2[r]
            l += 1
            r += 1
        if l < len(word1):
            s += word1[l:]
        if r < len(word2):
            s += word2[l:]
        
        return s
