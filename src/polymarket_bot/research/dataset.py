from dataclasses import dataclass
from typing import Iterable

@dataclass
class MarketSample:
    timestamp: int
    price_open: float
    price_now: float
    label: int


def build_label(price_open: float, price_close: float) -> int:
    return int(price_close >= price_open)


def split_walk_forward(samples: list[MarketSample], train_ratio: float = 0.7):
    cut = int(len(samples) * train_ratio)
    return samples[:cut], samples[cut:]
