# 33. Search in Rotated Sorted Array

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        curr = 0
        
        while(curr <= r):
            if nums[curr] == 0:
                nums[l], nums[curr] = nums[curr], nums[l]
                if curr == l:
                    curr += 1
                l += 1
            elif nums[curr] == 2:
                nums[r], nums[curr] = nums[curr], nums[r]
                r -= 1
            else:
                curr += 1
