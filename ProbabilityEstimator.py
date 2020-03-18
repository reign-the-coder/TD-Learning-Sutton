import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt
import sys

xB = np.array([1, 0, 0, 0, 0])
xC = np.array([0, 1, 0, 0, 0])
xD = np.array([0, 0, 1, 0, 0])
xE = np.array([0, 0, 0, 1, 0])
xF = np.array([0, 0, 0, 0, 1])
x = np.array([xB, xC, xD, xE, xF])
lambdaVal = 0.0
alphaVal = 0.0
trueProbabilities = [.166666666667, .3333333333, .5, .66666666667, .83333333333]
epsilon = 0.001


def main():
    with open('rmse3.txt', 'a') as f:
        rmse = []
        for i in range(100):
            fileName = "TrainingSet" + str(i) + ".txt"
            #error = noUpdatingPerSequence(fileName)
            error = updatingSequences(fileName)
            print(error)
            rmse.append(error)
        f.write("alpha: " + str(alphaVal) + " lambda: " + str(lambdaVal) + " RMSE: " + str(np.mean(rmse)) + "\n")
        #f.write(str(np.mean(rmse)) + ", ")


def noUpdatingPerSequence(fileName):
    global alphaVal, lambdaVal
    alphaVal = float(sys.argv[1])
    lambdaVal = float(sys.argv[2])
    weights = [0.5, 0.5, 0.5, 0.5, 0.5]

    with open(fileName, 'r') as f:
        content = f.readlines()
        delta = 0.0
        while True:
            for line in content:
                states = []
                for c in line.strip():
                    states.append(toInt(c))
                delta += deltaW(states, weights)
            weights = np.add(weights, delta)
            if np.sum(delta) < epsilon:
                break
            delta = 0.0
    rms = sqrt(mean_squared_error(trueProbabilities, weights))
    return rms



def updatingSequences(fileName):
    global alphaVal, lambdaVal
    alphaVal = float(sys.argv[1])
    lambdaVal = float(sys.argv[2])
    weights = [0.5, 0.5, 0.5, 0.5, 0.5]

    with open(fileName, 'r') as f:
        content = f.readlines()
        print(content)
        for line in content:
            states = []
            for c in line.strip():
                states.append(toInt(c))
            print(states)
            delta = deltaW(states, weights)
            weights = np.add(weights, delta)
            print(weights)
    rms = sqrt(mean_squared_error(trueProbabilities, weights))
    return rms


def toInt(char):
    return {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6
    }.get(char)


def deltaW(states, weights):
    steps = len(states)
    delta_w = np.zeros(5)
    for j in range(steps - 1):
        if j == steps - 2:
            part1 = np.multiply(alphaVal, (reward(states[j + 1]) - weights[states[j] - 1]))
        else:
            part1 = np.multiply(alphaVal, (weights[states[j + 1] - 1] - weights[states[j] - 1]))
        sum = 0
        if lambdaVal == 0.0:
            sum = x[states[j] - 1]
        else:
            for i in range(j+1):
                sum += pow(lambdaVal, j-i) * x[states[i] - 1]
        delta_w = np.add(delta_w, np.multiply(part1, sum))
    return delta_w


def reward(i):
    if i == 6:
        return 1.0
    else:
        return 0.0


if __name__ == '__main__':
    main()