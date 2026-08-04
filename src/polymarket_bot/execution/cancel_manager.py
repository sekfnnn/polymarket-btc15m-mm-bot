class CancelManager:
    def __init__(self):
        self.cancelled = False

    def cancel_all(self):
        self.cancelled = True

    def is_cancelled(self):
        return self.cancelled
