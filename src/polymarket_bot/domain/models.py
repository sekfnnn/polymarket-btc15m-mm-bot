from dataclasses import dataclass
from typing import Optional

@dataclass
class MarketEvent:
    market_id: str
    price: float
    timestamp: float

@dataclass
class Signal:
    side: str
    probability: float
    edge: float

@dataclass
class Order:
    side: str
    price: float
    size: float
    market_id: Optional[str] = None

@dataclass
class Trade:
    side: str
    price: float
    size: float
    pnl: float = 0.0
