#Question 2b
import matplotlib.pyplot as plt
import pandas as pd
import math

def yFunction(rTrue, rFalse):
    total = rTrue + rFalse
    return rTrue / total


def calculateError(numOfAcceptedSamples, frequencyOfToleratedErrors):
    val = frequencyOfToleratedErrors / 2
    numerator = -1 * math.log(val)
    denominator = 2 * numOfAcceptedSamples
    return math.sqrt(numerator / denominator)

def calculateProbabilities():
    data = pd.read_csv("./rs_1.csv")
    array = data.to_numpy()
    y = []
    y_plus_error = []
    y_minus_error = []
    rTrue = 0
    rFalse = 0
    for value in array:
        if value[0] == 1:
            rTrue += 1
        if value[0] == 2:
            rFalse += 1
        estimatedProbability = yFunction(rTrue, rFalse)
        numOfAcceptedSamples = rTrue + rFalse
        error = calculateError(numOfAcceptedSamples, 0.05)
        y.append(estimatedProbability)
        y_plus_error.append(estimatedProbability + error)
        y_minus_error.append(estimatedProbability - error)

    plotGraphs(y, y_plus_error, y_minus_error)



def plotGraphs(y, y_plus_error, y_minus_error):
    x = []
    for i in range(1, 100000):
        x.append(i)
    # plotting the points
    plt.plot(x, y, color='blue', linestyle='solid', linewidth=1,
             marker=',', markerfacecolor='blue', markersize=2)
    plt.plot(x, y_plus_error, color='green', linestyle='solid', linewidth=1,
             marker=',', markerfacecolor='green', markersize=2)
    plt.plot(x, y_minus_error, color='red', linestyle='solid', linewidth=1,
             marker=',', markerfacecolor='red', markersize=2)

    # setting x and y axis range
    plt.ylim(0, 1)
    plt.xlim(1, 100000)
    plt.xscale('log')
    # naming the x axis
    plt.xlabel('Number of samples')
    # naming the y axis
    plt.ylabel('P(R = T | s+, w+) With +/- Error')

    # giving a title to my graph
    plt.title('Q2. (b)')

    # function to show the plot
    plt.show()


calculateProbabilities()