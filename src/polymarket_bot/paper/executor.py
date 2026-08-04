from dataclasses import dataclass


@dataclass
class PaperFill:
    side: str
    price: float
    size: float


class PaperExecutor:
    def __init__(self):
        self.trades = []

    def execute(self, order):
        fill = PaperFill(
            side=order.side,
            price=order.price,
            size=order.size,
        )
        self.trades.append(fill)
        return fill
