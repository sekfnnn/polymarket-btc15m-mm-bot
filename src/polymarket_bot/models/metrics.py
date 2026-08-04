from math import sqrt

def sharpe(returns):
    if not returns:
        return 0.0
    mean=sum(returns)/len(returns)
    variance=sum((x-mean)**2 for x in returns)/len(returns)
    if variance == 0:
        return 0.0
    return mean/sqrt(variance)
