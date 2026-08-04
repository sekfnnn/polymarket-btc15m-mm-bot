from dataclasses import dataclass
from time import time


@dataclass
class MarketEvent:
    symbol: str
    price: float
    timestamp: float = time()


@dataclass
class SignalEvent:
    side: str
    probability: float
    fair_price: float
