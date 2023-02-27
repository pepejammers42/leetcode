# 2225. Find Players With Zero or One Losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        seen = set()
        zero, one = [], []

        for m in matches:
            d[m[1]] += 1
            seen.add(m[1])
            seen.add(m[0])

        for v in seen:
            if v not in d:
                zero.append(v)
            if d[v] == 1:
                one.append(v)
        return [sorted(zero), sorted(one)]
