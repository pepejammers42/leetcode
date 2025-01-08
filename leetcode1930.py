class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        # aabca
        # ^
        # left: a, right: a(2) b(1) c(1)
        # aabca
        #  ^
        # left a(2), right: a(1) b(1) c(1)

        res = set()
        left = set()
        right = Counter(s)

        for l in s:
            right[l] -= 1
            for c in left:
                if right[c] > 0:
                    res.add((l, c))
            left.add(l)
        return len(res)
