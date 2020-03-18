import random

def main():
    getTrainingSets()


def getTrainingSets():
    trainingSet = 0
    trainingSets = 0
    while trainingSets < 100:
        fileName = "TrainingSet" + str(trainingSets) + ".txt"
        f = open(fileName, "w")
        while trainingSet < 10:
            walk = ""
            currentState = 3
            while currentState != 0 and currentState != 6:
                walk += toString(currentState)
                percent = random.uniform(0.0, 1.0)
                if percent > 0.50:
                    currentState += 1
                else:
                    currentState -= 1
            walk += toString(currentState)
            trainingSet += 1
            f.write(walk)
            f.write("\n")
        trainingSets += 1
        trainingSet = 0



def toString(num):
    return {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G'
    }.get(num)



if __name__ == '__main__':
    main()