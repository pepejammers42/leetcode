class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for s in strs:
            key = [0] * 26
            for ch in s:
                key[ord(ch) - 97] += 1
            d[tuple(key)].append(s)
        return d.values()
