class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pf = ""
        
        strs.sort()
        f, l = strs[0], strs[-1]
        
        for i in range(len(f)):
            if f[i] != l[i]:
                break
            pf += f[i]
        return pf 
