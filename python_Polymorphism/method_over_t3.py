class Employee:
    def salary(self):
        print("Basic Salary")

class Developer(Employee):
    def salary(self):
        print("Salary = 50000")

class Manager(Employee):
    def salary(self):
        print("Salary = 80000")

emp1 = Developer()
emp2 = Manager()

emp1.salary()
emp2.salary()

