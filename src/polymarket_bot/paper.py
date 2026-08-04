from dataclasses import dataclass

@dataclass
class PaperTrade:
    side: str
    price: float
    size: float
    outcome: str | None = None

class PaperEngine:
    def __init__(self):
        self.trades=[]

    def submit(self, trade: PaperTrade):
        self.trades.append(trade)

    def pnl(self):
        result=0.0
        for t in self.trades:
            if t.outcome == t.side:
                result += t.size*(1-t.price)
            elif t.outcome:
                result -= t.size*t.price
        return result
