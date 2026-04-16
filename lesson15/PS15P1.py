#CIS 106 Session 14 Assignment - Classes and Objects --- ALisher Moldoshev

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def bonus(self):
        bonusRate = float(input('Enter bonus rate: '))
        return bonusRate * self.pay

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.fullname())
print(emp_1.bonus())
print(emp_1.email)