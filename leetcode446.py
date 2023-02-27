# 446. Arithmetic Slices II - Subsequence

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in range(len(nums))]
        r =  0
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1+dp[j][diff]
                r += dp[j][diff]
        return r
