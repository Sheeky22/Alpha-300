
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = []
        self.total = 0

    def next(self, val: int) -> float:

        self.queue.append(val)
        self.total += val

        if len(self.queue) > self.size:
            removed = self.queue.pop(0)
            self.total -= removed

        return self.total / len(self.queue)
