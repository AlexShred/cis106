#CIS 106 Session 12 Assignment - Static Arrays --- Moldoshev Alisher

lastNames = []
scores = []

with open("data.txt", "r") as f:
    for line in f:
        name, score = line.split()
        lastNames.append(name)
        scores.append(int(score))

def highestScore(lastnames, scores):
    high_var = 0
    high_index = 0
    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i

    print("Highest score:", lastnames[high_index], high_var)

def lowestScore(lastnames, scores):
    low_var = 999
    low_index = 0
    for i in range(len(scores)):
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    print("Lowest score:", lastnames[low_index], low_var)

highestScore(lastNames, scores)
lowestScore(lastNames, scores)