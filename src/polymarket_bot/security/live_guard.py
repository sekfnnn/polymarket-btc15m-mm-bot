class LiveGuard:
    def __init__(self, enabled: bool = False):
        self.enabled = enabled

    def can_trade(self) -> bool:
        return self.enabled

    def require_confirmation(self):
        if not self.enabled:
            raise RuntimeError('Live trading disabled')
