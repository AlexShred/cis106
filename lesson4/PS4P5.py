#Alisher Moldoshev --- 01.29.2026 --- assignment 4

userLastName = input('Enter your last name: ')
userNumberOfDependents = int(input('Enter your number of dependents: '))
userGrossIncome = int(input('Enter your gross income: '))

adjustedGross = userGrossIncome - (userNumberOfDependents * 12000)

if adjustedGross > 50000:
    taxRate = 0.2
else:
    taxRate = 0.1

incomeTax = adjustedGross * taxRate

if incomeTax < 0:
    incomeTax = 100

print(userLastName, 'your gross income is', userGrossIncome,
      'numer of dependents is', userNumberOfDependents,
      'adjusted gross income is', adjustedGross,
      'income tax is', incomeTax)
