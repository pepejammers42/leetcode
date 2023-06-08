class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for r in grid:
            idx = bisect_left(r, -1)
            res += len(r) - idx
        return res