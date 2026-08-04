from dataclasses import dataclass

@dataclass
class MakerQuote:
    price: float
    size: float
    post_only: bool = True


def should_quote(probability: float, price: float, min_edge: float = 0.02) -> bool:
    return probability - price >= min_edge


def build_quote(probability: float, tick: float = 0.01):
    price = probability - 0.02
    return round(price / tick) * tick
