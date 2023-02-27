# 1704. Determine if String Halves Are Alike

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vos = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        m = len(s)//2
        
        def count(s):
            c = 0
            
            for ch in s:
                if ch in vos:
                    c+= 1 
            return c
        
        return count(s[:m]) == count(s[m:])
