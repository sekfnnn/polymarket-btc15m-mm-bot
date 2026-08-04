class KillSwitch:
    def __init__(self, max_loss: float = 6.0):
        self.max_loss = max_loss

    def allowed(self, pnl: float) -> bool:
        return pnl > -self.max_loss
