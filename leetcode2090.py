class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        
        if k == 0:
            return nums
        
        n = len(nums)
        if 2 * k + 1 > n:
            return res
        
        curr = sum(nums[:2*k + 1])
        res[k] = curr // (2*k+1)
        
        for i in range(2*k+1, n):
            curr += nums[i] - nums[i-(2*k+1)]
            res[i-k] = curr// (2*k+1)

        return res