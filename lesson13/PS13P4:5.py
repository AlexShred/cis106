#CIS 106 Session 12 Assignment - Static Arrays --- Moldoshev Alisher

lastName = []
average = []

with open('data4.txt', 'r') as f:
    for line in f:
        name, avg = line.split()
        lastName.append(name)
        average.append(float(avg))

def printEverything(lastName, average):
    for name, avg in zip(lastName, average):
        print(name, avg)

def searchPlayer(lastName, average, inpName):
    found = False
    for i in range(len(lastName)):
        if lastName[i] == inpName:
            print(lastName[i], average[i])
            found = True
            break
    if not found:
        print("Name not found")

printEverything(lastName, average)

while True:
    inpName = input("Enter player last name: ")
    searchPlayer(lastName, average, inpName)
    cont = input('Do you wish to continue? (y/n): ')
    if cont == 'n':
        break
