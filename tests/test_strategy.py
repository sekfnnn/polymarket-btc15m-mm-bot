from polymarket_bot.strategy.model import estimate_probability


def test_probability_bounds():
    p = estimate_probability(0.0)
    assert 0 <= p <= 1
