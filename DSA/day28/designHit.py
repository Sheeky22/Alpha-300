class HitCounter:

    def __init__(self):
        self.queue = []

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:

        while self.queue and self.queue[0] <= timestamp - 300:
            self.queue.pop(0)

        return len(self.queue)
