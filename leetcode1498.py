class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 1000000007
        res = 0
        
        l = 0
        while l < len(nums) and nums[l] < target:
            loc = bisect_right(nums, target - nums[l], l)
            if loc > l:
                res += pow(2, loc - l - 1, mod)
            l += 1
        return res % mod
