from dataclasses import dataclass
from datetime import datetime

@dataclass
class TradeRecord:
    timestamp: datetime
    side: str
    price: float
    size: float
    pnl: float = 0.0

class TradeJournal:
    def __init__(self):
        self.records = []

    def add(self, trade: TradeRecord):
        self.records.append(trade)

    def total_pnl(self):
        return sum(x.pnl for x in self.records)
