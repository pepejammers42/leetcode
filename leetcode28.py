# 28. Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        
        while l < len(haystack):
            if haystack[l] == needle[0]:
                cnt = 0
                while cnt < len(needle):
                    if l + cnt >= len(haystack) or haystack[l + cnt]  != needle[cnt]:
                        break
                    if cnt == len(needle) - 1:
                        return l
                    cnt += 1
            l += 1
        return -1
