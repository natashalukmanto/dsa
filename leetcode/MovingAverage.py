from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self._sum = 0
        self._length = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self._sum += val
        self._length += 1

        if self._length > self.size:
            self._sum -= self.queue.popleft()
            self._length -= 1

        return self._sum / self._length


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
