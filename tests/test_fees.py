from polymarket_bot.fees import FeeModel


def test_crypto_fee():
    fee = FeeModel(0.07)
    assert round(fee.fee_per_share(0.5), 6) == 0.0175


def test_invalid_price():
    fee = FeeModel()
    try:
        fee.fee_per_share(1.2)
        assert False
    except ValueError:
        assert True
