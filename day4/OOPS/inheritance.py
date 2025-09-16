class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name:{self.name}\nSalary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary,dep):
        super().__init__(name, salary)
        self.dep = dep
    
    def display(self):
        print(f"Name:{self.name}\nSalary: {self.salary}\nDepartment: {self.dep}")  


emp = Employee("Harika",90000)
emp.display()

print()

man = Manager("Rishika",89000,"Tech")
man.display()