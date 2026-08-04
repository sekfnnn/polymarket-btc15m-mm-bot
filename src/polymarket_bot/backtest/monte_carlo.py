import random

def simulate(values, runs=1000):
    results=[]
    for _ in range(runs):
        results.append(sum(random.choice(values) for _ in values))
    return results
