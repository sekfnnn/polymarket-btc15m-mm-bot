from dataclasses import dataclass


@dataclass(frozen=True)
class FeeModel:
    rate: float = 0.07

    def fee_per_share(self, price: float) -> float:
        if not 0 < price < 1:
            raise ValueError("price must be between 0 and 1")
        return self.rate * price * (1 - price)

    def taker_cost(self, price: float, slippage: float = 0.0) -> float:
        return price + self.fee_per_share(price) + slippage


def expected_value(probability: float, price: float, fee: float = 0.0) -> float:
    return probability - price - fee
