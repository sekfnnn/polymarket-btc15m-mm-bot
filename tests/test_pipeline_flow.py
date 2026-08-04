from polymarket_bot.execution.position_guard import PositionGuard


def test_position_guard():
    guard = PositionGuard(10)
    assert guard.allow(5)
    guard.update(5)
    assert not guard.allow(6)
