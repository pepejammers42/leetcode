class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return False if len(s) == len(nums) else True
