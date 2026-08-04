from dataclasses import dataclass

@dataclass
class BacktestResult:
    trades: int
    pnl: float

class BacktestRunner:
    def run(self, trades):
        pnl = sum(t.pnl for t in trades)
        return BacktestResult(trades=len(trades), pnl=pnl)
