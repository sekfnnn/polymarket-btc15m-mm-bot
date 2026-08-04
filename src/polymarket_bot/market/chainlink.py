from dataclasses import dataclass

@dataclass
class ChainlinkTick:
    price: float
    timestamp_ms: int

class ChainlinkFeed:
    def __init__(self):
        self.last=None

    def update(self,tick:ChainlinkTick):
        self.last=tick

    def age_ms(self,now_ms:int):
        if self.last is None:
            return None
        return now_ms-self.last.timestamp_ms
