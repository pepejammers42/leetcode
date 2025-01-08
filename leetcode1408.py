class Node:
    def __init__(self) -> None:
        self.childs = {}


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def find(self, word) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.childs:
                return False
            curr = curr.childs[c]
        return True

    def ins(self, word) -> None:
        curr = self.root

        for c in word:
            curr = curr.childs.setdefault(c, Node())


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words_sorted = sorted(words, key=lambda x: -len(x))
        t = Trie()
        res = []

        for w in sorted(words, key=lambda x: -len(x)):
            if t.find(w):
                res.append(w)
            for i in range(len(w)):
                t.ins(w[i:])

        return res
