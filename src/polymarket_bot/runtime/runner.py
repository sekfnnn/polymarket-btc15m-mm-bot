from dataclasses import dataclass


@dataclass
class RuntimeResult:
    signal: object | None
    order: object | None
    trade: object | None


class RuntimeRunner:
    def __init__(self, engine=None, executor=None):
        self.engine = engine
        self.executor = executor

    def handle_event(self, event):
        if self.engine is None:
            return RuntimeResult(None, None, None)

        signal = self.engine.process(event)

        if signal is None or self.executor is None:
            return RuntimeResult(signal, None, None)

        trade = self.executor.execute(signal)
        return RuntimeResult(signal, signal, trade)
