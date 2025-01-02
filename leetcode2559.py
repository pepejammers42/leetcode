class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        # pfix
        # ["aba","bcb","ece","aa","e"]
        # 0       1     1     2    3   4
        # [0,2] = diff(0, 3) = 2 - 0 = 2.
        # [l, r] = diff(l, r+1)

        pfix = [0] * (len(words) + 1)
        v = "aeiou"
        for i, w in enumerate(words):
            pfix[i + 1] = pfix[i] + (w[0] in v and w[-1] in v)

        return [pfix[r + 1] - pfix[l] for l, r in queries]
