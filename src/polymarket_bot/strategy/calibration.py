def calibrate(probability: float, confidence: float = 0.95) -> float:
    uncertainty = (1-confidence) * 0.1
    return max(0.01, min(0.99, probability - uncertainty))
