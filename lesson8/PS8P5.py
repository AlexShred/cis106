#Session 8 Assignment Problems - Introduction to Functions ---- Alisher Moldoshev

contq = input('Do you want to continue? (yes/no): ')

totalSum = 0

def tuitionOwed(codeDist, creditHours):
    if codeDist == "I":
        sumPerHour = 250
    else:
        sumPerHour = 550

    total = sumPerHour * creditHours

    return total

while contq == 'yes':
    studentName = input('Enter student name: ')
    codeDist = input('Enter code district (I/O): ').upper
    creditHours = int(input('Enter credit hours: '))

    tuition = tuitionOwed(codeDist, creditHours)

    print(f"{studentName} - {tuition:.2f}")

    totalSum += tuition

    contq = input('Do you want to continue? (yes/no): ')

print("Total sum: ", f"{totalSum:.2f}")