# 2161. Partition Array According to Given Pivot

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        pivots = []
        right = []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                pivots.append(num)
            else:
                right.append(num)
        return left + pivots + right  
