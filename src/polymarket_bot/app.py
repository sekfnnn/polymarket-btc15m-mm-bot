from .config_loader import load_config
from .execution.risk_guard import RiskGuard


def run():
    config = load_config()
    risk = RiskGuard(
        bankroll=config.get("risk", {}).get("bankroll", 30),
    )
    return risk.allow()


if __name__ == "__main__":
    print(run())
