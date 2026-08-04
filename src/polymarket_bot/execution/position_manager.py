from dataclasses import dataclass


@dataclass
class Position:
    token: str
    size: float
    avg_price: float


class PositionManager:
    def __init__(self):
        self.positions = []

    def add(self, position: Position):
        self.positions.append(position)

    def exposure(self):
        return sum(p.size * p.avg_price for p in self.positions)
