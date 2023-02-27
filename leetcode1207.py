# 1207. Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)

        for item in arr:
            d[item] += 1

        visited = set()
        for k,v in d.items():
            if v in visited:
                return False
            visited.add(v)
        return True
