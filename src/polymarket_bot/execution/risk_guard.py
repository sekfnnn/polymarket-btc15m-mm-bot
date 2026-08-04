from dataclasses import dataclass


@dataclass
class RiskGuard:
    bankroll: float = 30.0
    max_loss: float = 6.0
    pnl: float = 0.0
    enabled: bool = True

    def update(self, pnl_change: float):
        self.pnl += pnl_change
        if self.pnl <= -self.max_loss:
            self.enabled = False

    def allow(self) -> bool:
        return self.enabled
