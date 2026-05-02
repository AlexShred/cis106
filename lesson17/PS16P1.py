#Session 16  MOLDOSHEV ALISHER

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay, bonus_rate=0.0):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        self.bonus_rate = bonus_rate

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def calculate_bonus(self):
        return self.pay * self.bonus_rate

    def total_compensation(self):
        return self.pay + self.calculate_bonus()


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang, bonus_rate=0.0):
        super().__init__(first, last, pay, bonus_rate)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    def long_term_bonus(self):
        return self.pay * 0.4

class Executive(Manager):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay, employees)

    def executive_bonus(self):
        return self.pay * 2

    def long_term_bonus(self):
        return self.pay * 0.5


exec1 = Executive('Alex', 'Shred', 100000)

print(exec1.fullname())
print('Salary:', exec1.pay)
print('Executive Bonus:', exec1.executive_bonus())
print('Long Term Bonus:', exec1.long_term_bonus())