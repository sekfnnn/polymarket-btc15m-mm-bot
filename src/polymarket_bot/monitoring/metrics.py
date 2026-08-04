from dataclasses import dataclass


@dataclass
class Metrics:
    trades: int = 0
    pnl: float = 0.0
    wins: int = 0

    def record(self, pnl: float):
        self.trades += 1
        self.pnl += pnl
        if pnl > 0:
            self.wins += 1

    @property
    def win_rate(self):
        if self.trades == 0:
            return 0.0
        return self.wins / self.trades
