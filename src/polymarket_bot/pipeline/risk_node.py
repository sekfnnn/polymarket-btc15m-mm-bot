class RiskNode:
    def __init__(self, guard=None):
        self.guard = guard

    def check(self, signal):
        if self.guard is None:
            return True
        return self.guard.allow(signal)
