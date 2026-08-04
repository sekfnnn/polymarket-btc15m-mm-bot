from polymarket_bot.probability import conservative_probability
from polymarket_bot.risk import fractional_kelly


def test_probability_bounds():
    assert conservative_probability(0.5) == 0.48


def test_kelly_zero_when_no_edge():
    assert fractional_kelly(0.5, 0.5) == 0


def test_kelly_positive():
    assert fractional_kelly(0.6, 0.5) > 0
