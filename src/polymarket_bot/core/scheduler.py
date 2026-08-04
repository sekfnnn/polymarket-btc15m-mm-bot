import asyncio


class Scheduler:
    def __init__(self):
        self.tasks = []

    def add(self, coroutine):
        self.tasks.append(coroutine)

    async def run(self):
        if self.tasks:
            await asyncio.gather(*self.tasks)
