from dataclasses import dataclass

from polymarket_bot.execution.order_pipeline import OrderPipeline


@dataclass
class Order:
    price: float
    size: float


class AllowValidator:
    def validate(self, order):
        return order.size > 0


class AllowPosition:
    def allow(self, order):
        return True


def test_order_pipeline_full_flow():
    pipeline = OrderPipeline(
        validator=AllowValidator(),
        position_guard=AllowPosition(),
    )

    result = pipeline.process(Order(0.5, 1))

    assert result.allowed
