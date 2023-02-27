# 380. Insert Delete GetRandom O(1)

class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.l.append(val)
            self.d[val] = len(self.l)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.d:
            i = self.d[val]
            self.d[self.l[-1]] = i
            self.l[i] = self.l[-1]
            self.d.pop(val)
            self.l.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
