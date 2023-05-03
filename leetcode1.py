class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for c, v in enumerate(nums):
            if target - v in d:
                return [c, d[target-v]]
            d[v] = c 
