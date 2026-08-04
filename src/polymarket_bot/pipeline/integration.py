class Pipeline:
    def __init__(self, collector=None, strategy=None, risk=None, execution=None):
        self.collector = collector
        self.strategy = strategy
        self.risk = risk
        self.execution = execution

    def on_market_event(self, event):
        signal = self.strategy.evaluate(event) if self.strategy else None
        if signal is None:
            return None

        if self.risk and not self.risk.allow():
            return None

        return self.execution.execute(signal) if self.execution else signal
