from dataclasses import dataclass


@dataclass
class FakeEvent:
    price: float


def test_fake_market_event_flow():
    event = FakeEvent(price=100000)
    assert event.price > 0
