import statistics
import math

data = [[0.5, 4, 112.1], [1, 7.75, 102.6], [1.5, 12.5, 103], [2, 16, 104.4], [2.5, 21, 112.5], [3, 21, 97], [3.5, 30.5, 115], [4, 37, 117.1]]

I = 2/5 * (173.5 - 31.6) / 1000 * (2.11 * .0254) ** 2 / 4
constants = 4 * math.pi ** 2 * 4.5 * I

def B(current):
    return current * .00137

def T(periods, time):
    return time / periods

def Mu(current, periods, time):
    return constants / T(periods, time) / B(current)

results = []
for trial in data:
    results.append(Mu(*trial))

print(results)
print(sum(results) / len(results))
print(statistics.stdev(results))