from dataclasses import dataclass

@dataclass
class Calibrator:
    uncertainty: float = 0.03

    def calibrate(self, probability: float) -> float:
        value = probability - self.uncertainty
        return max(0.01, min(0.99, value))
