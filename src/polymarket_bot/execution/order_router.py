from dataclasses import dataclass

@dataclass
class OrderRequest:
    side: str
    price: float
    size: float

class OrderRouter:
    def __init__(self, live=False):
        self.live = live

    def route(self, order: OrderRequest):
        if not self.live:
            return {"mode": "paper", "order": order}
        raise RuntimeError("Live execution disabled")
