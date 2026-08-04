from dataclasses import dataclass

@dataclass
class BaselineModel:
    uncertainty: float = 0.03

    def predict(self, market_probability: float) -> float:
        p = min(max(market_probability, 0.01), 0.99)
        return min(max(p, 0.01), 0.99)

    def conservative(self, probability: float) -> float:
        return max(0.01, probability - self.uncertainty)
