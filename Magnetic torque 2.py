import math
import statistics

def B(current):
    return .00137 * current

def T(halfPeriods, time):
    periods = halfPeriods / 2
    return time / periods

def Mu(current, halfPeriods, time):
    return I/B(current) * 4 * math.pi ** 2 / T(halfPeriods, time) ** 2

I = 2/5 * (173.5 - 31.6) / 1000 * (2.11 * .0254) ** 2 / 4

data = [[0.2, 10, 31.66], [0.4, 20, 35.5], [0.6, 23, 31.5], [0.8, 28, 32.4], [1, 39, 39.9], [1.2, 44, 32.7], [1.4, 56, 46.8], [1.6, 50, 39.3], [1.8, 44, 32.7], [2, 50, 34.9], [2.2, 50, 33.3], [2.4, 53, 33.7], [2.6, 54, 33.2], [2.8, 54, 31.9], [3.0, 50, 28.7], [3.2, 60, 33.3], [3.4, 70, 33.6], [3.6, 82, 42.5], [3.8, 60, 30.6]]

results = []
for trial in data:
    results.append(Mu(*trial))

print(results)
print(sum(results) / len(results))
print(statistics.stdev(results))
