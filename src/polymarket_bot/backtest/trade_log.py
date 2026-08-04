from dataclasses import dataclass
from datetime import datetime

@dataclass
class TradeRecord:
    timestamp: datetime
    side: str
    price: float
    size: float
    pnl: float = 0.0
