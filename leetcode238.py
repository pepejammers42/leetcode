class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        for n in range(1, len(nums)):
            res[n] = res[n-1] * nums[n-1]
        
        post = 1
        for n in range(len(nums)-1, -1, -1):
            res[n] = res[n] * post
            post *= nums[n]

        return res
