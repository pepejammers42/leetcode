# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([word for word in reversed(s.split())])
