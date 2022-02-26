class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = list()
        self.lastSum = 0
    def next(self, val: int) -> float:
        if len(self.queue) < self.size:
            self.lastSum += val
        else:
            self.lastSum -= self.queue.pop(0)
            self.lastSum += val
        self.queue.append(val)
        return self.lastSum / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)