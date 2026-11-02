
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1

        i = len(self.stack) - 1

        value = self.stack[i] + self.inc[i]

        if i > 0:
            self.inc[i - 1] += self.inc[i]

        self.stack.pop()
        self.inc.pop()

        return value

    def increment(self, k: int, val: int) -> None:
        i = min(k, len(self.stack)) - 1

        if i >= 0:
            self.inc[i] += val
