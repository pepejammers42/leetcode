# 739. Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        d = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while d and temperatures[i] > temperatures[d[-1]]:
                tmp = d.pop()
                result[tmp] = i - tmp
            d.append(i)
        return result
