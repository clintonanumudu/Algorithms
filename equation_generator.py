"""
A couple more things left to do:
3. Now also if below is the answer it should tell me the value of below
4. Same with arbitrary
"""

import time
import random

CORRECT_ANSWER = "2 - x % 2"
EPOCHS = 100

dataset = {
    1: 3,
    2: 4,
    3: 5,
    4: 6,
    5: 7,
    6: 8,
    7: 9,
    8: 10,
    9: 11,
    10: 12
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
    bestSolution = ""
    highestScore = 0
    equationScore = 0
    iterations = 1
    answer = None
    while (answer != out or equationScore < len(dataset)) and iterations <= EPOCHS * 10:
        equation = generateRandomEquation()
        answer = calculateString(equation, inp)
        print("[" + str(iterations) + "] " + bestSolution)
        iterations += 1
        equationScore = getEquationScore(equation, dataset)
        if equationScore > highestScore:
            highestScore = equationScore
            bestSolution = equation
        #time.sleep(0.1)
    
    if highestScore < len(dataset):
        print("\nThe solution could not be found.")
        print("Closest solution was:", str(bestSolution))
        percent = highestScore / len(dataset) * 100
        print("It has an accuracy of", percent, "%.\n")
    else:
        print("\nSolution To The Dataset:", str(bestSolution), "\n")

equationCreator(dataset)
