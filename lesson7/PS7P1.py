#Moldoshev Alisher ----Session 7 Assignment Problems – Looping Logic 2 and Reading Data from the Keyboard and Files ---

principleAmount = float(input('Enter the principal amount: '))
interestRate = float(input('Enter the interest rate: '))

year = 1
totalintrst = 0

while year <= 5 :
        annualInterestRate = principleAmount * interestRate
        endingBalannce = principleAmount + annualInterestRate
        print('Year:', {year})
        print(f'Beginning balance : {principleAmount:.2f}')
        print(f'Endining balance: {endingBalannce:.2f}')

        totalintrst += annualInterestRate
        principleAmount = endingBalannce
        year += 1

print(f'Total interest rate: {totalintrst:.2f}')