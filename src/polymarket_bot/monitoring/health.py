from dataclasses import dataclass


@dataclass
class Health:
    websocket: bool
    oracle: bool
    risk_ok: bool

    @property
    def ready(self) -> bool:
        return self.websocket and self.oracle and self.risk_ok
