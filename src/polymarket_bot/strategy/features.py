from dataclasses import dataclass

@dataclass
class Features:
    spread: float
    imbalance: float
    volatility: float
    oracle_age: float


def build_features(spread: float, imbalance: float, volatility: float, oracle_age: float) -> Features:
    return Features(spread, imbalance, volatility, oracle_age)
