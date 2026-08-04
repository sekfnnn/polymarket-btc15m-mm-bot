from dataclasses import dataclass


@dataclass
class RiskManager:
    bankroll: float
    max_fraction: float = 0.05

    def max_position(self) -> float:
        return self.bankroll * self.max_fraction

    def allow(self, cost: float) -> bool:
        return cost <= self.max_position()


def fractional_kelly(probability: float, price: float, fraction: float = 0.05) -> float:
    if probability <= price:
        return 0.0
    kelly = (probability - price) / (1 - price)
    return kelly * fraction
