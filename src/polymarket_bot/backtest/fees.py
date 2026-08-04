def polymarket_fee(price: float, rate: float = 0.07) -> float:
    return rate * price * (1 - price)


def net_edge(probability: float, price: float, rate: float = 0.07) -> float:
    return probability - price - polymarket_fee(price, rate)
