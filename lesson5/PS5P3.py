#Moldoshev Alisher --- CIS 106 Session 5 Assignment

principleAmount = int(input('Enter the principle amount '))
years = int(input("Enter years to maturity: "))

if principleAmount > 100000 and years == 5:
    interestRate = 0.06
elif (principleAmount <= 100000 and principleAmount >= 50000 and years == 5):
    interestRate = 0.04
elif (principleAmount <= 100000 and principleAmount >= 50000 and years == 10):
    interestRate = 0.05
else:
    interestRate = 0.02

frstYearRate = principleAmount * interestRate

print("The principle amount is:", principleAmount,
    "\nThe interest rate is:", interestRate,
    "\nThe first year interest is:", frstYearRate)