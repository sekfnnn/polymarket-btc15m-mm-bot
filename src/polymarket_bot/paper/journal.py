from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class JournalEntry:
    timestamp: datetime
    trade: object


class TradeJournal:
    def __init__(self):
        self.entries = []

    def record(self, trade):
        self.entries.append(
            JournalEntry(datetime.utcnow(), trade)
        )

    def all(self):
        return self.entries
