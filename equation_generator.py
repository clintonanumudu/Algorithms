import time
import random

CORRECT_ANSWER = "2 - x % 2"

dataset = {
    1: 1,
    2: 2,
    3: 1,
    4: 2,
    5: 1,
    6: 2,
    7: 1,
    8: 2,
    9: 1,
    10: 2
}

def generateRandomEquation():
    valueList = ["bel", 0, 1, 2, "arb", "x"]
    operationList = ["+", "-", "*", "/", "%"]
    randomValue = random.choice(valueList)
    equationString = str(randomValue)
    operationAmount = random.randint(1, 2)
    for i in range(operationAmount):
        randomOperation = random.choice(operationList)
        randomValue = random.choice(valueList)
        equationString += " " + randomOperation + " " + str(randomValue)
    return equationString

def calculateString(string, inp):
    string = string.replace("x", str(inp))
    randomBelowValue = round(random.uniform(0.1, 0.9), 1)
    string = string.replace("bel", str(randomBelowValue))
    randomArbitraryValue = random.randint(3, 100)
    string = string.replace("arb", str(randomArbitraryValue))
    try:
        answer = eval(string)
        return answer
    except Exception as e:
        return 0

# The score is most likely either 100% or 0%
def getEquationScore(equation, dataset):
    equationScore = 0
    for key, value in dataset.items():
        answer = calculateString(equation, key)
        if answer == value:
            equationScore += 1
        else:
            return equationScore
    return equationScore

def equationCreator(dataset):
    # Show the data point that was picked before beginning
    randomDataPoint = random.choice(list(dataset.keys()))
    inp = randomDataPoint
    out = dataset[inp]
    print(inp, out)

    # Pick random data point and generate equations until works
    bestSolution = None
    answer = None
    equationScore = 0
    iterations = 1
    while answer != out or equationScore < 3:
        equation = generateRandomEquation()
        answer = calculateString(equation, inp)
        print(bestSolution)
        iterations += 1
        highestScore = 0
        equationScore = getEquationScore(equation, dataset)
        if equationScore > highestScore:
            highestScore = equationScore
            bestSolution = equation
        #time.sleep(0.1)
    
    print("Solution To The Dataset: ", str(bestSolution))

equationCreator(dataset)
