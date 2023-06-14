class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []

        i = 0
        while i < len(nums):
            
            l = nums[i]
            while i + 1 < len(nums) and nums[i+1] - 1 == nums[i]:
                i += 1
            
            if l == nums[i]:
                res.append(str(l))
            else:
                res.append(str(l) + "->" + str(nums[i]))
            
            i += 1

        return res