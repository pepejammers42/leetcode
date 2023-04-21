class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        r = [False] * len(candies)
        g = max(candies)
        for i,v in enumerate(candies):
            if v + extraCandies >= g:
                r[i] = True
        return r
