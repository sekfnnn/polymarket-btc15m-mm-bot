import math


def normal_cdf(x: float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def btc_up_probability(log_return: float, variance: float, horizon: float) -> float:
    if variance <= 0 or horizon <= 0:
        return 0.5
    z = log_return / math.sqrt(variance * horizon)
    return max(0.0, min(1.0, normal_cdf(z)))


def conservative_probability(probability: float, error: float = 0.02) -> float:
    return max(0.0, min(1.0, probability - error))
