class ExecutionNode:
    def __init__(self, executor=None):
        self.executor = executor

    def execute(self, order):
        if self.executor is None:
            return None
        return self.executor.route(order)
