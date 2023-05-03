class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tmp = set(nums)
        res = 0
        
        for n in tmp:
            l = 0
            if n-1 not in tmp:
                while n+l in tmp:
                    l += 1
                res = max(l, res)
        return res
