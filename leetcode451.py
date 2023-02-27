# 451. Sort Characters By Frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        
        for ch in s:
            d[ch] += 1
        
        s = sorted(d.items(), key= lambda x: -x[1])
        
        r = ''
        for k, v in s:
            r += k * v
        return r
