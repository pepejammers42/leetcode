class Node:
    def __init__(self):
        self.child = {}
        self.end = False
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = Node()
            curr = curr.child[ch]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            if ch not in curr.child:
                return False
            curr = curr.child[ch]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            if ch not in curr.child:
                return False
            curr = curr.child[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
