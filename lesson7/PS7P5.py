#Moldoshev Alisher ----Session 7 Assignment Problems – Looping Logic 2 and Reading Data from the Keyboard and Files ---

with open('students.txt', 'w') as file:
    cont = 'yes'

    while cont == 'yes':
        student = input('Enter Student Name: ')
        district = input('Enter District(I or O): ')
        credit = float(input('Enter Credit: '))


        file.write(f"{student}\n")
        file.write(f"{district}\n")
        file.write(f"{credit}\n")

        cont = input('Continue? (Y/N): ')

studentAmount = 0
sum = 0

with open('students.txt', 'r') as file:
    while True:
        student = file.readline().strip()
        if not student:
            break

        district = file.readline().strip()
        credit = float(file.readline().strip())

        if district == "I":
            creditcost = 250
        else:
            creditcost = 500

        toPay = creditcost * credit

        print(f'Student: {student}')
        print(f'District: {district}')
        print(f'Credit: {credit}')
        print(f'ToPay: {toPay}')

        sum += toPay
        studentAmount += 1

print(f'Total: {sum}')
print(f'Number of students: {studentAmount}')
