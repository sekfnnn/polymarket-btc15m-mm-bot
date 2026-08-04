class TradingEngine:
    def __init__(self, collector=None, strategy=None, risk=None, executor=None):
        self.collector = collector
        self.strategy = strategy
        self.risk = risk
        self.executor = executor

    def process(self, event):
        if self.strategy is None:
            return None

        signal = self.strategy.evaluate(event)

        if self.risk and not self.risk.allow():
            return None

        if self.executor:
            return self.executor.execute(signal)

        return signal
