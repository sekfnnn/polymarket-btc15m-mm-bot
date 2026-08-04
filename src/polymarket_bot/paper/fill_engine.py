class FillEngine:
    def __init__(self, latency_ms=100):
        self.latency_ms = latency_ms

    def simulate(self, order):
        return {
            "filled": True,
            "side": order.side,
            "price": order.price,
            "size": order.size,
        }
