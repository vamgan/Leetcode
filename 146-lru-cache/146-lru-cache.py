from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.size = abs(capacity)
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            self.put(key, val)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
        else:
            if len(self.cache) == self.size:
                self.cache.popitem(last = False)
            self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)