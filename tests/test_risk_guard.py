from polymarket_bot.execution.risk_guard import RiskGuard


def test_risk_blocks_after_loss():
    guard = RiskGuard(max_loss=6)
    assert guard.allowed(-7) is False


def test_risk_allows_small_loss():
    guard = RiskGuard(max_loss=6)
    assert guard.allowed(-1) is True
