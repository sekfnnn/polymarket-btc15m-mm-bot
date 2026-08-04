from dataclasses import dataclass

@dataclass
class Market:
    token_id:str
    question:str
    tick_size:float
    min_order_size:int

class CLOBClient:
    def __init__(self,base_url:str):
        self.base_url=base_url

    async def get_market(self,token_id:str):
        raise NotImplementedError

    async def place_order(self,order):
        raise NotImplementedError
