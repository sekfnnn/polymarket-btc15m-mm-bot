class OrderValidator:
    def __init__(self, max_size=5):
        self.max_size = max_size

    def validate(self, order):
        if order.price <= 0:
            return False
        if order.size <= 0:
            return False
        if order.size > self.max_size:
            return False
        return True
