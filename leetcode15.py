class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for c, v in enumerate(nums):
            if c > 0 and nums[c-1] == v:
                continue
            
            l, r = c + 1, len(nums) - 1
            while l < r:
                tmp = v + nums[l] + nums[r]
                if tmp > 0:
                    r -= 1
                elif tmp < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            
        return res 
