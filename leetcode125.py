class Solution:
    def isPalindrome(self, s: str) -> bool:
        filt = ''.join(ch for ch in s if ch.isalnum()).lower()
        
        return filt == filt[::-1]
        # l, r = 0, len(filt)-1
        
        # while l < r:
            # if filt[l] != filt[r]:
                # return False
            # l += 1
            # r -= 1

        # return True
