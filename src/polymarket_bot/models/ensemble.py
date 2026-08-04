from dataclasses import dataclass

@dataclass
class EnsembleModel:
    market_weight: float = 0.5
    feature_weight: float = 0.5

    def combine(self, market: float, feature: float) -> float:
        value = self.market_weight * market + self.feature_weight * feature
        return min(max(value, 0.01), 0.99)
