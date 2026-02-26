#Session 8 Assignment Problems - Introduction to Functions ---- Alisher Moldoshev

contq = input('Do you want to continue? (yes/no): ')

totalGross = 0

def payRate(jobCode):
    if jobCode == 'L':
        return 25
    elif jobCode == 'A':
        return 30
    elif jobCode == 'J':
        return 50
    else:
        return 0

while contq == 'yes':
    emplName = input('Enter employee name: ')
    jobCode = input('Enter the job code: ')
    hoursWorked = int(input('Enter the hours worked: '))

    payCode = payRate(jobCode)

    if hoursWorked <= 40:
        total = hoursWorked * payCode
    else:
        total = 40 * payCode + (hoursWorked - 40) * payCode * 1.5

    totalGross += total

    print(f"{emplName} gross pay: {total:.2f}")

    contq = input('Do you want to continue? (yes/no): ')

print('Total gross pay:', f"{totalGross:.2f}")