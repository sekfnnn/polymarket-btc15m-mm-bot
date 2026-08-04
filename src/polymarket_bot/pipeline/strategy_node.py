class StrategyNode:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def evaluate(self, data):
        if self.strategy is None:
            return None
        return self.strategy.evaluate(data)
