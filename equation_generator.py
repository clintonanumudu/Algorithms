"""
A couple more things left to do:
5. If answer is close to value but decimal, award half a point
6. Try an extremely difficult one on Google Colab
6. Optimize code by moving functions to other files
7. Transform into machine learning library
"""

import time
import random

CORRECT_ANSWER = "2 - x % 2"
EPOCHS = 200

dataset = {
    1: 0.2,
    2: 0.4,
    3: 0.6,
    4: 0.8,
    5: 1,
    6: 1.2,
    7: 1.4,
    8: 1.6,
    9: 1.8,
    10: 2
}

def countDecimals(value):
    # Convert the value to a string
    value_str = str(value)
    
    # Check if the value has a decimal point
    if '.' in value_str:
        # Find the position of the decimal point
        decimal_position = value_str.index('.')
        
        # Count the number of digits after the decimal point
        decimal_places = len(value_str) - decimal_position - 1
        return decimal_places
    else:
        # If there's no decimal point, return 0
        return 0

def generateRandomEquation():
    valueList = ["bel", 0, 1, 2, "arb", "x"]
    operationList = ["+", "-", "*", "/", "%"]
    randomValue = random.choice(valueList)
    equationString = str(randomValue)
    operationAmount = random.randint(1, 4)
    for i in range(operationAmount):
        randomOperation = random.choice(operationList)
        randomValue = random.choice(valueList)
        equationString += " " + randomOperation + " " + str(randomValue)
    randomBelowValue = round(random.uniform(0.1, 0.9), 1)
    equationString = equationString.replace("bel", str(randomBelowValue))
    randomArbitraryValue = random.randint(3, 100)
    equationString = equationString.replace("arb", str(randomArbitraryValue))
    return equationString

def calculateString(string, inp):
    string = string.replace("x", str(inp))
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
        if round(answer, countDecimals(value)) == value:
            equationScore += 1
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
    while equationScore < len(dataset) and iterations <= EPOCHS * 10:
        equation = generateRandomEquation()
        print("[" + str(iterations) + "] " + bestSolution)
        iterations += 1
        equationScore = getEquationScore(equation, dataset)
        if equationScore > highestScore:
            highestScore = equationScore
            bestSolution = equation
        time.sleep(0.01)

    if highestScore < len(dataset):
        print("\nThe solution could not be found.")
        print("Closest solution was:", str(bestSolution))
        percent = highestScore / len(dataset) * 100
        print("It has an accuracy of", percent, "%.\n")
    else:
        print("\nSolution To The Dataset:", str(bestSolution), "\n")

equationCreator(dataset)

#print(getEquationScore("0.2*x", dataset))
