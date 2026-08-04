from dataclasses import dataclass

@dataclass
class BacktestReport:
    trades: int
    pnl: float
    sharpe: float

    def profitable(self) -> bool:
        return self.pnl > 0
