import time

class Heartbeat:
    def __init__(self, timeout_seconds: float = 10):
        self.timeout_seconds = timeout_seconds
        self.last = time.monotonic()

    def touch(self):
        self.last = time.monotonic()

    def alive(self) -> bool:
        return time.monotonic() - self.last < self.timeout_seconds
