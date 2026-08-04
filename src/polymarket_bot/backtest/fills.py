from dataclasses import dataclass

@dataclass
class QueueState:
    queue_ahead: float
    order_size: float
    executed_volume: float = 0.0

    def filled(self) -> bool:
        return self.executed_volume >= self.queue_ahead + self.order_size


def simulate_fill(queue_ahead: float, size: float, traded_volume: float) -> bool:
    return traded_volume >= queue_ahead + size
