from dataclasses import dataclass

@dataclass
class Level:
    price: float
    size: float

@dataclass
class OrderBook:
    bids: list[Level]
    asks: list[Level]

    @property
    def mid(self):
        if not self.bids or not self.asks:
            return None
        return (self.bids[0].price + self.asks[0].price) / 2

    @property
    def spread(self):
        if not self.bids or not self.asks:
            return None
        return self.asks[0].price - self.bids[0].price
