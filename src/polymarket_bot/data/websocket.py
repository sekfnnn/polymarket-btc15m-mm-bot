class MarketWebSocket:
    def __init__(self):
        self.connected = False
        self.last_message = None

    def connect(self):
        self.connected = True

    def update(self, message):
        self.last_message = message

    def healthy(self):
        return self.connected and self.last_message is not None
