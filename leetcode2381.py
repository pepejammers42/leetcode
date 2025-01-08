class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """

        # s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
        # [0,1,0] => [1,0,-1,0]
        # [1,2,1] => [1,-1,-1,1]
        # [0,2,1] => [0,-1,-1,2]
        # final stuffs => [0,0,1,2] => 'ace'

        pfix = [0] * (len(s) + 1)
        res = [ord(c) for c in s]

        for l, r, d in shifts:
            pfix[l] += -1 if d else 1
            pfix[r + 1] += 1 if d else -1

        diff = 0
        for i in range(len(pfix), 1, -1):
            diff += pfix[i - 1]
            res[i - 2] = chr(((res[i - 2] - 97 + diff) % 26) + 97)

        return "".join(res)
