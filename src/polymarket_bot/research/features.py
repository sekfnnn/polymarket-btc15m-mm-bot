def spread_feature(bid: float, ask: float) -> float:
    return ask - bid


def imbalance_feature(bid_volume: float, ask_volume: float) -> float:
    total = bid_volume + ask_volume
    if total == 0:
        return 0.0
    return (bid_volume - ask_volume) / total
