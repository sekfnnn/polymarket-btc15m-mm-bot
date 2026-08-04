from dataclasses import dataclass

@dataclass
class Result:
    pnl: float
    trades: int

class BacktestEngine:
    def __init__(self):
        self.pnl = 0.0
        self.trades = 0

    def add_trade(self, pnl: float):
        self.pnl += pnl
        self.trades += 1

    def result(self):
        return Result(self.pnl, self.trades)
