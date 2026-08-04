from dataclasses import dataclass

@dataclass
class CollectorNode:
    source: object | None = None

    def update(self, event):
        return event
