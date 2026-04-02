#CIS 106 Session 12 Assignment - Static Arrays --- Moldoshev Alisher

lastNames = ['John', 'Blake', 'Allison', 'Adams', 'Lee', 'Smith', 'White', 'Endrik', 'Gomes', 'Madara']

scores = [90, 80, 70, 65, 70, 65, 70, 65, 70, 65]

def printLastnames(lastnames):
    for lastname in lastnames:
        print(lastname)

def printLastnamesReverse(lastnames):
    for lastname in lastnames[::-1]:
        print(lastname)

def printLastNamesScore(lastnames, scores):
    for lastname, score in zip(lastnames, scores):
        print(f'{lastname}: {score}')

#printLastnames(lastNames)
#printLastnamesReverse(lastNames)
printLastNamesScore(lastNames, scores)