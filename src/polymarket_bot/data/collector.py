from dataclasses import dataclass
from datetime import datetime

@dataclass
class MarketTick:
    price: float
    timestamp: datetime

class MarketCollector:
    def __init__(self):
        self.ticks = []

    def add(self, tick: MarketTick):
        self.ticks.append(tick)

    def latest(self):
        return self.ticks[-1] if self.ticks else None
