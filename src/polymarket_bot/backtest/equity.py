class EquityCurve:
    def __init__(self, initial=30.0):
        self.values = [initial]

    def add(self, pnl):
        self.values.append(self.values[-1] + pnl)

    @property
    def peak(self):
        return max(self.values)

    def drawdown(self):
        return self.peak - self.values[-1]
