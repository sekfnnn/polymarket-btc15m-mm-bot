from dataclasses import dataclass

@dataclass
class ChainlinkPrice:
    price: float
    timestamp: float

class ChainlinkAdapter:
    def __init__(self):
        self.latest = None

    def update(self, price: float, timestamp: float):
        self.latest = ChainlinkPrice(price, timestamp)

    def age(self, now: float):
        if self.latest is None:
            return None
        return now - self.latest.timestamp
