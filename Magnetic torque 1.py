import math
import statistics

def getMu(data):
    for trial in data:
        trial.append((trial[3][0] * totalMass[0] / 1000 * 9.81 / math.tan(math.radians(trial[2][0])) / trial[4][0], None))
        print(trial[-1][0])

def getField(data):
    for trial in data:
        trial.append((trial[1][0] * .00137, trial[1][1] * .00137))

def getR(data, initialMeasurements):
    for trial in data:
        value = distFromCenter[0] + (initialMeasurements[1][0] * initialMeasurements[0][0] / 2 + (initialMeasurements[0][0] - initialMeasurements[3][0] / 2 - trial[0][0]) * initialMeasurements[2][0]) / totalMass[0]
        uncertainty = None
        trial.append((value, uncertainty))

def addUncertainty(rawData):
    data = []
    for point in rawData:
        data.append([(point[0], 0.05), (point[1], 0.05), (point[2], 5)])

    return data

initialMeasurements = ((5.508 * .0254, 0.005 * .0254), (0.975, 0.005), (0.375 * .0254, 0.005 * .0254), (1.400, 0.005), (2.110 * .0254, 0.005 * .0254), (0.5 * .0254, 0.05 * .0254), (4.14 * .0254, 0.005 * .0254), (31.6, 0.05), (173.5, 0.05))
totalMass = (initialMeasurements[1][0] + initialMeasurements[3][0], (initialMeasurements[1][1] ** 2 + initialMeasurements[3][1] ** 2) ** (1 / 2))
distFromCenter = (initialMeasurements[6][0] + initialMeasurements[5][0] + initialMeasurements[4][0] / 2 - initialMeasurements[0][0], (initialMeasurements[6][1] ** 2 + initialMeasurements[5][1] ** 2 + (initialMeasurements[4][1] / 2) ** 2 + initialMeasurements[0][1] ** 2) ** (1 / 2))

rawData = ((0.5, 4.15, 47), (0.5, 4.2, 64), (1, 3.90, 58), (1, 3.95, 62), (1, 4, 69), (1, 4.05, 74), (1.5, 3.6, 74), (1.5, 3.7, 84), (1.5, 3.8, 87), (1.5, 3.9, 88), (2, 3.2, 67), (2, 3.3, 83), (2, 3.6, 87), (2, 3.9, 89))

data = addUncertainty(rawData)

getR(data, initialMeasurements)
getField(data)
getMu(data)
print('\n', sum([trial[-1][0] for trial in data]) / len([trial[-1][0] for trial in data]))
print(statistics.stdev([trial[-1][0] for trial in data]))