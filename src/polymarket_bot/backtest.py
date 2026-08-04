from dataclasses import dataclass


@dataclass
class Trade:
    price: float
    size: int
    won: bool


def pnl(trade: Trade) -> float:
    if trade.won:
        return trade.size * (1 - trade.price)
    return -trade.size * trade.price


def run(trades: list[Trade]) -> float:
    return sum(pnl(t) for t in trades)
