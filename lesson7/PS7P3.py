#Moldoshev Alisher ----Session 7 Assignment Problems – Looping Logic 2 and Reading Data from the Keyboard and Files ---

with open('salary.txt', 'w') as file:
    file.write('LastName, salary, bonus\n')

contq = input("Start cycle?:")

sumBonus = 0

while contq == 'yes':

    lastName = input('Enter last name: ')
    salary = float(input('Enter salary: '))

    if salary >= 100000:
        bonus = salary * 0.2
        total = salary + bonus
    elif salary >= 50000:
        bonus = salary * 0.15
        total = salary + bonus
    else:
        bonus = salary * 0.10
        total = salary + bonus

    sumBonus += bonus

    with open('salary.txt', 'a') as file:
        file.write(f'{lastName}, {salary:.2f}, {bonus:.2f}\n')

    contq = input("Continue?:")

print('Sum of all bonus:', sumBonus)
