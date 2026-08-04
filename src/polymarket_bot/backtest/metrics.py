from dataclasses import dataclass
from math import sqrt

@dataclass
class Metrics:
    pnl: float
    trades: int


def sharpe(returns):
    if len(returns) < 2:
        return 0.0
    avg = sum(returns) / len(returns)
    variance = sum((x-avg)**2 for x in returns)/(len(returns)-1)
    if variance == 0:
        return 0.0
    return avg / sqrt(variance)
