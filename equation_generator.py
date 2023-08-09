"""
A couple more things left to do:
6. Decimals should give half points not full points
7. It should find patterns where finding a pattern is literally impossible
8. It should work with multiple inputs
9. Optimize code by moving functions to other files
10. Transform into machine learning library
"""

import time
import random
import sympy as sp

CORRECT_ANSWER = "x * x - 3 % x % 3 * 3"
EPOCHS = 10000000000000

dataset = {
    2: 20,
    7: 49,
    11: 121,
    16: 256
}

def simplifyResult(equation):
    simplified = str(sp.sympify(equation))
    simplified = simplified.replace("*", " * ")
    simplified = simplified.replace("/", " / ")
    simplified = simplified.replace("%", " % ")
    simplified = simplified.rewrite(sp.Mod, sp.mod)
    return simplified

def countDecimals(value):
    value_str = str(value)
    if '.' in value_str:
        decimal_position = value_str.index('.')
        decimal_places = len(value_str) - decimal_position - 1
        return decimal_places
    else:
        return 0

def generateRandomEquation():
    valueList = ["arb", "x"]
    operationList = ["+", "-", "*", "/", "%"]
    randomValue = random.choice(valueList)
    equationString = str(randomValue)
    operationAmount = random.randint(1, 6)
    for i in range(operationAmount):
        randomOperation = random.choice(operationList)
        randomValue = random.choice(valueList)
        equationString += " " + randomOperation + " " + str(randomValue)
    randomArbitraryValue = random.randint(0, 10)
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
        if answer == value or (round(answer, countDecimals(value)) == value and str(answer).count("0000000000") > 0):
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
        print("[" + str(iterations) + "] " + bestSolution + "[" + equation + "]")
        iterations += 1
        equationScore = getEquationScore(equation, dataset)
        if equationScore > highestScore:
            highestScore = equationScore
            bestSolution = equation

    #bestSolution = simplifyResult(bestSolution)

    if highestScore < len(dataset):
        print("\nThe solution could not be found.")
        print("Closest solution was:", str(bestSolution))
        percent = highestScore / len(dataset) * 100
        print("It has an accuracy of", percent, "%.\n")
    else:
        print("\nSolution To The Dataset:", str(bestSolution), "\n")

equationCreator(dataset)

#print(getEquationScore("0.3 + x * 0.1", dataset))
