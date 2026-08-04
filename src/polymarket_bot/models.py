from dataclasses import dataclass


@dataclass(frozen=True)
class MarketState:
    price: float
    seconds_left: int
    bid: float
    ask: float


@dataclass(frozen=True)
class Signal:
    probability: float
    side: str
    edge: float


@dataclass(frozen=True)
class Order:
    side: str
    price: float
    size: int
    post_only: bool = True
