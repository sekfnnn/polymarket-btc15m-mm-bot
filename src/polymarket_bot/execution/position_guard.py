class PositionGuard:
    def __init__(self, max_position):
        self.max_position = max_position
        self.position = 0

    def allow(self, size):
        return abs(self.position + size) <= self.max_position

    def update(self, size):
        self.position += size
