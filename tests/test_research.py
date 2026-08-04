from polymarket_bot.research.dataset import build_label
from polymarket_bot.research.features import imbalance_feature


def test_label():
    assert build_label(100, 101) == 1


def test_imbalance():
    assert imbalance_feature(10, 10) == 0
