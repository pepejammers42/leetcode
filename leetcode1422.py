class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 011101
        # z = 1
        # o = 4
        res = 0
        zero = 0
        one = s.count("1")

        for i in range(len(s) - 1):
            if s[i] == "0":
                zero += 1
            else:
                one -= 1
            res = max(res, zero + one)

        return res
