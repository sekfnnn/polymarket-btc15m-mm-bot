from dataclasses import dataclass

@dataclass
class PaperTrade:
    side: str
    price: float
    size: float

class PaperTrader:
    def __init__(self):
        self.trades = []

    def execute(self, trade: PaperTrade):
        self.trades.append(trade)
        return trade
