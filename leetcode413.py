# 413. Arithmetic Slices

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [None] * (len(nums)-1)
        r = 0
        
        for i in range(1, len(nums)):
            dp[i-1] = nums[i] - nums[i-1]

        inc = 1
        for i in range(1, len(dp)):
            if dp[i] == dp[i-1]:
                r += inc
                inc += 1
            else:
                inc = 1
        
        return r
