from dataclasses import dataclass
import math

@dataclass
class Statistics:
    returns: list[float]

    def sharpe(self):
        if not self.returns:
            return 0.0
        mean = sum(self.returns) / len(self.returns)
        variance = sum((x-mean)**2 for x in self.returns) / len(self.returns)
        if variance == 0:
            return 0.0
        return mean / math.sqrt(variance)

    def total_return(self):
        return sum(self.returns)
