# Inheritance
# Problem: Display Employee Details

class Employee:
    def employee_details(self):
        self.name = input("Enter employee name: ")
        self.salary = int(input("Enter salary: "))


class Manager(Employee):
    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


manager = Manager()
manager.employee_details()
manager.display()
class Manager(Employee):
    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


manager = Manager()
manager.employee_details()
manager.display()