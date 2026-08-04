from polymarket_bot.execution.order_pipeline import OrderPipeline


class AllowValidator:
    def validate(self, order):
        return True


class AllowPosition:
    def allow(self, order):
        return True


def test_order_pipeline_allows():
    pipeline = OrderPipeline(AllowValidator(), AllowPosition())
    result = pipeline.validate(object())
    assert result.allowed
