from dataclasses import dataclass


@dataclass
class SlippageModel:
    base_bps: float = 2.0

    def cost(self, price: float, volatility: float = 0.0) -> float:
        return price * (self.base_bps / 10000.0 + volatility)
