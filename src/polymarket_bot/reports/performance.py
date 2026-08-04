from dataclasses import dataclass

@dataclass
class PerformanceReport:
    trades: int
    pnl: float
    wins: int

    @property
    def win_rate(self) -> float:
        if self.trades == 0:
            return 0.0
        return self.wins / self.trades

    def to_dict(self):
        return {
            "trades": self.trades,
            "pnl": self.pnl,
            "wins": self.wins,
            "win_rate": self.win_rate,
        }
