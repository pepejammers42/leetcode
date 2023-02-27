# 2389. Longest Subsequence With Limited Sum

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # [4,5,2,1]
        # [3, 10, 21]
        # [1,3,7,12]
        
        result = []
        nums.sort()
        pf_sum = [nums[0]]
        for n in nums[1:]:
            pf_sum.append(pf_sum[-1]+n)
        
        for q in queries:
            result.append(bisect_right(pf_sum, q)) 
        return result
