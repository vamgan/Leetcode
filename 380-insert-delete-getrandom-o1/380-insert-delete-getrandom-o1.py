import random
class RandomizedSet:

    def __init__(self):
        self.randomSet = dict()
        self.arr = list()

    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False
        self.randomSet[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        
        if val in self.randomSet:
            idx = self.randomSet[val]
            self.randomSet[self.arr[-1]] = idx
            self.randomSet.pop(val)
            self.arr[-1], self.arr[idx] = self.arr[idx], self.arr[-1]
            self.arr.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()