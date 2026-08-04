from .features import Features


def predict_probability(features: Features) -> float:
    score = 0.5
    score += -features.spread * 0.1
    score += features.imbalance * 0.1
    score -= min(features.oracle_age / 1000, 0.05)
    return max(0.01, min(0.99, score))
