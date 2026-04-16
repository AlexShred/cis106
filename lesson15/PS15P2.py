class Student:

    def __init__(self, first, last, districtCode, classEnt):
        self.first = first
        self.last = last
        self.districtCode = districtCode
        self.classEnt = classEnt

    def tuitionRate(self):
        if self.districtCode == 'I':
            return 250
        elif self.districtCode == 'O':
            return 500
        else:
            print('Invalid District Code')
            return 0

    def price(self):
        return self.classEnt * self.tuitionRate()

first = input('Enter first name: ')
last = input('Enter last name: ')
districtCode = input('Enter district code (I or O): ').upper()
classEnt = int(input('Enter enrolled credits: '))

stu_1 = Student(first, last, districtCode, classEnt)

print(stu_1.price())
print('Student:', stu_1.first, stu_1.last)
print('Tuition owed: $', stu_1.price())