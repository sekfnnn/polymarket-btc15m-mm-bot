from enum import Enum

class OrderState(Enum):
    CREATED = "created"
    SENT = "sent"
    FILLED = "filled"
    CANCELLED = "cancelled"

