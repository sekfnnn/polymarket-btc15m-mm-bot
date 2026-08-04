def normalize_price(price: float) -> float:
    if price <= 0:
        raise ValueError('price must be positive')
    return float(price)


def normalize_probability(value: float) -> float:
    return min(max(float(value), 0.0), 1.0)
