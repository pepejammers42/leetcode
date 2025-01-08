class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [10,4,-8,7]
        # lr = 10 14 6 13
        # rl = 7 -1 3 13
        res = 0
        lr = 0
        rl = sum(nums)

        for i in range(len(nums) - 1):
            lr += nums[i]
            rl -= nums[i]

            if lr >= rl:
                res += 1
        return res
