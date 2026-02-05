#Moldoshev Alisher --- CIS 106 Session 5 Assignment

employeeLastName = input('Enter the employee last name ')
employeeSalary = int(input('Enter the employee salary '))
employeeJobLevel = int(input('Enter the employee job level '))

if employeeJobLevel >= 10:
    bonusRate = 0.25
elif employeeJobLevel >= 5 and employeeJobLevel <= 9:
    bonusRate = 0.20
else:
    bonusRate = 0.10

bonusAmount = employeeSalary * bonusRate
totalSAmount = employeeSalary + bonusAmount

print(employeeLastName, 'bonus amount is ', bonusAmount, 'total salary is ', totalSAmount)