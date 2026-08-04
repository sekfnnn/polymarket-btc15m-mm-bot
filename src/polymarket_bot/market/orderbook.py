from dataclasses import dataclass

@dataclass
class Level:
    price: float
    size: float

@dataclass
class OrderBook:
    bids: list[Level]
    asks: list[Level]

    def best_bid(self):
        return self.bids[0] if self.bids else None

    def best_ask(self):
        return self.asks[0] if self.asks else None

    def midpoint(self):
        if not self.bids or not self.asks:
            return None
        return (self.bids[0].price + self.asks[0].price) / 2

    def spread(self):
        if not self.bids or not self.asks:
            return None
        return self.asks[0].price - self.bids[0].price

    def imbalance(self):
        bid=sum(x.size for x in self.bids)
        ask=sum(x.size for x in self.asks)
        if bid+ask==0:
            return 0.0
        return (bid-ask)/(bid+ask)
